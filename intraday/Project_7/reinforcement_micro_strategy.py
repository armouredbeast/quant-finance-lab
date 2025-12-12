"""
reinforcement_micro_strategy.py
Tabular Q-Learning micro intraday strategy.

Usage:
 - Place a CSV named `price.csv` with columns Date,Close in same folder OR
 - Let the script generate synthetic GBM price series.
 - Run: python reinforcement_micro_strategy.py

Dependencies:
 - numpy, pandas, matplotlib, sklearn (for StandardScaler)
"""

import os
import math
import random
from collections import defaultdict
from dataclasses import dataclass
from typing import Tuple, List

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler

RNG = np.random.default_rng(42)
random.seed(42)

# -------------------------
# Environment
# -------------------------
@dataclass
class MicroEnv:
    prices: pd.Series  # indexed by datetime or integer
    transaction_cost: float = 0.0005  # proportion (e.g. 5 bps)
    slippage_penalty: float = 0.0002  # additional cost for switching position
    window_short: int = 5
    window_long: int = 20

    def reset(self):
        self.t = max(self.window_long, self.window_short)
        self.position = 0  # -1, 0, +1
        self.entry_price = None
        return self._get_state(self.t)

    def step(self, action: int) -> Tuple[Tuple[int,int,int,int], float, bool]:
        """
        action: -1,0,1 representing short/flat/long
        returns: state, reward, done
        """
        price = self.prices.iloc[self.t]
        prev_price = self.prices.iloc[self.t - 1]
        done = False

        # executed at close price of this timestep
        reward = 0.0

        # P&L from holding position from previous time to now
        reward += (price - prev_price) * self.position  # positive for long if price up

        # cost when changing position
        if action != self.position:
            # pay transaction cost on both close/open sides (approx)
            cost = self.transaction_cost * abs(action) * price
            reward -= cost
            # slippage penalty
            reward -= self.slippage_penalty * price

            # if we close a position realize P&L already captured via holding
            # set entry price for new position
            if action != 0:
                self.entry_price = price

        # update position
        self.position = action

        # advance time
        self.t += 1
        if self.t >= len(self.prices):
            done = True
            next_state = None
        else:
            next_state = self._get_state(self.t)

        return next_state, reward, done

    def _get_state(self, t: int) -> Tuple[int,int,int,int]:
        """
        Build discrete state:
         - short_return_bucket: sign of short term return over window_short (-1/0/1)
         - long_return_bucket: sign of long term return over window_long (-1/0/1)
         - vol_bucket: volatility bucket (0..n_vol-1)
         - position: -1/0/1
        """
        short_ret = (self.prices.iloc[t] - self.prices.iloc[t - self.window_short]) / self.prices.iloc[t - self.window_short]
        long_ret = (self.prices.iloc[t] - self.prices.iloc[t - self.window_long]) / self.prices.iloc[t - self.window_long]

        # buckets for returns
        def ret_bucket(x):
            if x > 0.002: return 1
            if x < -0.002: return -1
            return 0

        sr = ret_bucket(short_ret)
        lr = ret_bucket(long_ret)

        # volatility: std of returns over long window
        returns = self.prices.pct_change().iloc[t - self.window_long + 1:t + 1].dropna()
        vol = returns.std() if len(returns) > 0 else 0.0

        # discretize volatility into 3 buckets low/med/high
        if vol < 0.005:
            vb = 0
        elif vol < 0.02:
            vb = 1
        else:
            vb = 2

        pos = int(self.position)  # -1,0,1

        # map pos to 0,1,2 for consistent indexing
        pos_idx = pos + 1
        return (sr, lr, vb, pos_idx)  # tuple state

# -------------------------
# Utility: state -> index mapping
# -------------------------
class StateIndexer:
    def __init__(self):
        self.mapping = {}
        self.counter = 0

    def encode(self, state_tuple):
        # state_tuple is small (sr,lr,vb,pos_idx) where sr ∈ {-1,0,1}
        key = tuple(state_tuple)
        if key not in self.mapping:
            self.mapping[key] = self.counter
            self.counter += 1
        return self.mapping[key]

    def decode_all(self):
        # returns mapping for debugging
        return self.mapping

# -------------------------
# Q-Learning Agent (Tabular)
# -------------------------
class QAgent:
    def __init__(self, n_actions: int, alpha=0.1, gamma=0.99, eps=0.2):
        self.n_actions = n_actions
        self.alpha = alpha
        self.gamma = gamma
        self.eps = eps
        self.Q = defaultdict(lambda: np.zeros(self.n_actions))  # key -> action values

    def choose_action(self, state_idx):
        # epsilon-greedy
        if random.random() < self.eps:
            return random.randrange(self.n_actions)
        else:
            return int(np.argmax(self.Q[state_idx]))

    def update(self, s, a, r, s_next, done):
        q = self.Q[s][a]
        if done or s_next is None:
            target = r
        else:
            target = r + self.gamma * np.max(self.Q[s_next])
        self.Q[s][a] = q + self.alpha * (target - q)

    def save_policy(self, path="q_table.npy"):
        # simple save
        np.save(path, dict(self.Q))

# -------------------------
# Helpers: metrics & backtest
# -------------------------
def backtest_with_policy(prices: pd.Series, policy: dict, indexer: StateIndexer, env_kwargs=None):
    env = MicroEnv(prices, **(env_kwargs or {}))
    state = env.reset()
    s_idx = indexer.encode(state)
    pos_map = {0:-1, 1:0, 2:1}  # action idx -> true pos
    pnl = []
    positions = []
    ts = []
    while True:
        a_idx = policy.get(s_idx, 1)  # default flat if unseen
        action = pos_map[a_idx]
        next_state, reward, done = env.step(action)
        pnl.append(reward)
        positions.append(env.position)
        ts.append(env.t)
        if done:
            break
        s_idx = indexer.encode(next_state)

    pnl = np.array(pnl)
    cum = np.cumsum(pnl)
    returns = pnl  # per-step P&L
    # metrics
    ann_ret = (cum[-1] / prices.iloc[0]) * (252 * (24*60) / 1) if False else cum[-1]  # leave as raw P&L for intraday
    vol = np.std(returns) * np.sqrt(252) if len(returns) > 1 else 0.0
    sharpe = ann_ret / vol if vol > 0 else 0.0
    return dict(total_pnl=cum[-1], cum=cum, pnl_series=pnl, sharpe=sharpe, positions=positions, times=ts)

# -------------------------
# Training loop
# -------------------------
def train_q_agent(prices: pd.Series,
                  episodes=200,
                  alpha=0.1,
                  gamma=0.99,
                  eps_start=0.4,
                  eps_end=0.05,
                  eps_decay=0.995):
    indexer = StateIndexer()
    agent = QAgent(n_actions=3, alpha=alpha, gamma=gamma, eps=eps_start)
    env_template = MicroEnv(prices)
    eps = eps_start

    for ep in range(episodes):
        env = MicroEnv(prices,
                       transaction_cost=env_template.transaction_cost,
                       slippage_penalty=env_template.slippage_penalty,
                       window_short=env_template.window_short,
                       window_long=env_template.window_long)
        state = env.reset()
        s_idx = indexer.encode(state)
        total_reward = 0.0
        steps = 0
        done = False
        while not done:
            # map action idx to actual action -1/0/1
            a_idx = agent.choose_action(s_idx)
            pos_map = {0:-1, 1:0, 2:1}
            action = pos_map[a_idx]
            next_state, reward, done = env.step(action)
            total_reward += reward
            steps += 1
            s_next_idx = None if next_state is None else indexer.encode(next_state)
            agent.update(s_idx, a_idx, reward, s_next_idx, done)
            if not done:
                s_idx = s_next_idx

        # decay epsilon
        agent.eps = max(eps_end, agent.eps * eps_decay)
        if (ep+1) % max(1, episodes//10) == 0:
            print(f"Ep {ep+1}/{episodes} | total_reward={total_reward:.2f} | eps={agent.eps:.3f} | Qstates={indexer.counter}")

    return agent, indexer

# -------------------------
# Data loader: CSV or synthetic
# -------------------------
def load_prices_from_csv(path="price.csv", n=2000):
    if os.path.exists(path):
        df = pd.read_csv(path, parse_dates=["Date"], dayfirst=True)
        df = df.sort_values("Date").reset_index(drop=True)
        return df["Close"]
    else:
        print(f"[info] {path} not found. Generating synthetic GBM ({n} points).")
        return generate_gbm(n=n)

def generate_gbm(S0=100.0, mu=0.0, sigma=0.02, n=2000, dt=1/390):
    # dt chosen as fraction of trading day (intraday), but we keep simple
    prices = [S0]
    for i in range(1, n):
        z = RNG.normal()
        Sprev = prices[-1]
        S = Sprev * math.exp((mu - 0.5 * sigma**2) * dt + sigma * math.sqrt(dt) * z)
        prices.append(S)
    return pd.Series(prices)

# -------------------------
# Main runnable demo
# -------------------------
def main():
    prices = load_prices_from_csv()
    prices = prices.reset_index(drop=True)
    print("Loaded prices:", len(prices))

    # quick sanity plot
    # prices.plot(title="Price series"); plt.show()

    # Train agent
    agent, indexer = train_q_agent(prices,
                                   episodes=200,
                                   alpha=0.1,
                                   gamma=0.98,
                                   eps_start=0.4,
                                   eps_end=0.02,
                                   eps_decay=0.98)

    # Produce greedy policy
    policy = {}
    for state_tuple, idx in indexer.mapping.items():
        # choose argmax
        a = int(np.argmax(agent.Q[idx]))
        policy[idx] = a

    # Backtest policy
    stats = backtest_with_policy(prices, policy, indexer)
    print("Backtest total PnL:", stats["total_pnl"])
    print("Approx Sharpe (ad-hoc):", stats["sharpe"])

    # Plot cumulative PnL
    plt.figure(figsize=(10,4))
    plt.plot(stats["cum"], label="Cumulative PnL")
    plt.title("Tabular Q-Learning micro-strategy - cumulative PnL")
    plt.xlabel("Time step")
    plt.ylabel("P&L")
    plt.legend()
    plt.grid(True)
    plt.show()

    # Save Q-table
    agent.save_policy("q_table.npy")
    print("Saved Q-table to q_table.npy")
    # Optionally dump mapping
    mapping_df = pd.DataFrame.from_records([(k, v) for k, v in indexer.mapping.items()], columns=["state","idx"])
    mapping_df.to_csv("state_mapping.csv", index=False)
    print("Saved state mapping to state_mapping.csv")

if __name__ == "__main__":
    main()