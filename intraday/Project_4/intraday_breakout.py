"""
Intraday Breakout (5-min)
- Uses yfinance 5-min bars (may be limited to recent history)
- Strategy: if price breaks above today's opening range high -> go long until close
- Very simple; serves as prototype for intraday logic
"""
import os
import pandas as pd
import numpy as np
import yfinance as yf
import matplotlib.pyplot as plt

TICKER="AAPL"
PERIOD="7d"
INTERVAL="5m"
OUTPUT="reports"
os.makedirs(OUTPUT, exist_ok=True)

def download_intraday(ticker):
    df = yf.download(ticker, period=PERIOD, interval=INTERVAL, progress=False)
    if df.empty:
        raise RuntimeError("No intraday data (yfinance limits).")
    return df

def build_signals(df):
    df = df.copy()
    df['date'] = df.index.date
    out = []
    for d,group in df.groupby('date'):
        group = group.copy()
        open_price = group['Open'].iloc[0]
        # define opening range (first 12 bars = first hour)
        or_high = group['High'].iloc[:12].max()
        # breakout: price crosses above OR high
        group['signal'] = (group['High'] > or_high).astype(int)
        out.append(group)
    res = pd.concat(out)
    return res

def backtest(df):
    df['position'] = df['signal'].shift(1).fillna(0)
    df['ret'] = df['Close'].pct_change().fillna(0)
    df['pnl'] = df['position'] * df['ret']
    equity = (1+df['pnl']).cumprod()
    return df, equity

def main():
    df = download_intraday(TICKER)
    df_s = build_signals(df)
    df_b, equity = backtest(df_s)
    plt.figure(figsize=(10,5))
    plt.plot(equity)
    plt.title("Intraday Breakout — Equity (prototype)")
    plt.grid(True)
    plt.savefig(os.path.join(OUTPUT,"intraday_equity.png"))
    df_b.to_csv(os.path.join(OUTPUT,"intraday_trace.csv"))
    print("Saved:",os.path.join(OUTPUT,"intraday_equity.png"), os.path.join(OUTPUT,"intraday_trace.csv"))

if __name__=="__main__":
    main()