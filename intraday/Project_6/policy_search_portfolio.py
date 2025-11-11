"""
Policy-search portfolio agent (lightweight)
- Optimizes static weights with random search / hill climbing on historical returns.
- Serves as a tiny 'RL-like' experiment without heavy frameworks.
"""
import os
import numpy as np
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

TICKERS=["AAPL","MSFT","GOOGL"]
START="2022-01-01"
OUTPUT="reports"
os.makedirs(OUTPUT, exist_ok=True)

def download(tickers):
    data={}
    for t in tickers:
        df=yf.download(t,start=START,progress=False)
        data[t]=df['Close']
    prices=pd.concat(data,axis=1).dropna()
    prices.columns=tickers
    return prices

def return_series(prices):
    return prices.pct_change().dropna()

def evaluate(weights, rets):
    port = (rets * weights).sum(axis=1)
    # objective: Sharpe (annualized)
    mean = port.mean()*252
    vol = port.std()*np.sqrt(252)
    return mean/vol if vol>0 else -999

def policy_search(rets, n_iter=2000, step=0.1):
    n = rets.shape[1]
    # start equal weights
    w = np.ones(n)/n
    best = w.copy()
    best_score = evaluate(best, rets)
    for i in range(n_iter):
        # propose small random perturbation and renormalize
        cand = best + np.random.normal(scale=step, size=n)
        cand = np.clip(cand, 0, None)
        cand /= (cand.sum() + 1e-9)
        score = evaluate(cand, rets)
        if score > best_score:
            best_score = score
            best = cand
    return best, best_score

def main():
    prices = download(TICKERS)
    rets = return_series(prices)
    best_w, score = policy_search(rets, n_iter=2000, step=0.05)
    print("Best weights:", {t:round(w,4) for t,w in zip(TICKERS,best_w)}, "score", round(score,4))
    port = (rets * best_w).sum(axis=1)
    cum=(1+port).cumprod()
    plt.figure(figsize=(10,5))
    plt.plot(cum)
    plt.title("Policy-Search Portfolio (toy) — cumulative")
    plt.grid(True)
    plt.savefig(os.path.join(OUTPUT,"policy_search_cum.png"))
    print("Saved:", os.path.join(OUTPUT,"policy_search_cum.png"))

if __name__=="__main__":
    main()