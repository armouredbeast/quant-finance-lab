"""
Backtester with slippage and transaction cost in one script.
- Simple signal: 20d MA cross above 50d MA -> long; below -> flat
- Transaction costs: proportional (bps) + per-trade slippage
- Reports P&L, annualized metrics, saves equity curve
"""
import os
import numpy as np
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

TICKER="AAPL"
START="2022-01-01"
OUTPUT="reports"
PROPORTIONAL_COST=0.0005   # 5 bps round-trip
SLIPPAGE=0.0007            # 7 bps slippage per trade
os.makedirs(OUTPUT, exist_ok=True)

def download(ticker):
    df = yf.download(ticker, start=START, progress=False)
    return df['Close'].dropna()

def generate_signals(prices):
    ma20 = prices.rolling(20).mean()
    ma50 = prices.rolling(50).mean()
    signal = (ma20 > ma50).astype(int)
    signal = signal.fillna(0)
    return signal

def backtest(prices, signal):
    positions = signal.shift(1).fillna(0)
    rets = prices.pct_change().fillna(0)
    # gross P&L:
    pnl = positions * rets
    # transaction cost when position changes
    trades = positions.diff().abs()
    cost = trades * (PROPORTIONAL_COST + SLIPPAGE)
    net_pnl = pnl - cost
    equity = (1+net_pnl).cumprod()
    return net_pnl, equity

def metrics(series):
    # Ensure outputs are scalars, not pandas Series
    ann_ret = float(series.mean() * 252)
    ann_vol = float(series.std() * np.sqrt(252))
    sharpe = ann_ret / ann_vol if ann_vol > 0 else 0.0
    return ann_ret, ann_vol, sharpe

def main():
    prices = download(TICKER)
    signal = generate_signals(prices)
    net_pnl, equity = backtest(prices, signal)
    ann_ret, ann_vol, sharpe = metrics(net_pnl)
    print("AnnRet",round(ann_ret,4),"Vol",round(ann_vol,4),"Sharpe",round(sharpe,4))
    plt.figure(figsize=(10,5))
    plt.plot(equity)
    plt.title("Backtest w/ Costs — Equity Curve")
    plt.grid(True)
    plt.savefig(os.path.join(OUTPUT,"backtest_equity.png"))
    print("Saved:", os.path.join(OUTPUT,"backtest_equity.png"))

if __name__=="__main__":
    main()