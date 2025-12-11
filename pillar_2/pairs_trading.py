#!/usr/bin/env python3
"""
pairs_trading.py
Find cointegrated pairs using Engle-Granger and backtest a simple z-score mean-reversion strategy.
Usage: python pairs_trading.py
Outputs: reports/pairs_list.csv, reports/pairs_backtest.png
"""
import os, warnings
warnings.filterwarnings("ignore")

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf
from statsmodels.tsa.stattools import coint
from statsmodels.regression.linear_model import OLS
from statsmodels.tools.tools import add_constant

REPORTS = "reports"
os.makedirs(REPORTS, exist_ok=True)

def fetch_universe(tickers, start="2019-01-01"):
    df = yf.download(tickers, start=start, progress=False)["Close"].dropna()
    return df

def find_cointegrated_pairs(data, pvalue_threshold=0.05):
    n = data.shape[1]
    tickers = data.columns
    pairs = []
    for i in range(n):
        for j in range(i+1, n):
            s1 = data.iloc[:, i]
            s2 = data.iloc[:, j]
            score, pvalue, _ = coint(s1, s2)
            if pvalue < pvalue_threshold:
                pairs.append((tickers[i], tickers[j], pvalue))
    pairs_df = pd.DataFrame(pairs, columns=["t1","t2","pvalue"])
    return pairs_df

def backtest_pair(s1, s2, entry_z=2.0, exit_z=0.5):
    # compute spread residuals from regression s1 ~ s2
    res = OLS(s1, add_constant(s2)).fit()
    spread = s1 - (res.params[1]*s2 + res.params[0])
    zscore = (spread - spread.mean())/spread.std()
    pos = pd.Series(0, index=spread.index)
    # entry short spread (z > entry) -> short s1, long s2
    pos[zscore > entry_z] = -1
    pos[zscore < -entry_z] = 1
    pos[abs(zscore) < exit_z] = 0
    pos = pos.ffill().fillna(0)
    # P&L approximation on returns
    r1 = s1.pct_change().fillna(0)
    r2 = s2.pct_change().fillna(0)
    # simple unit-dollar neutral: pnl = pos * (r1 - beta*r2)
    beta = res.params[1]
    pnl = pos.shift(1) * (r1 - beta * r2)
    cum = (1 + pnl).cumprod() - 1
    return cum, zscore

def main():
    tickers = ["AAPL", "MSFT", "GOOGL", "AMZN"]
    data = fetch_universe(tickers)
    pairs = find_cointegrated_pairs(data)
    pairs.to_csv(f"{REPORTS}/pairs_list.csv", index=False)
    print("Pairs found:\n", pairs)
    if len(pairs) == 0:
        print("No cointegrated pairs found at threshold.")
        return

    # backtest first pair
    t1, t2 = pairs.iloc[0,0], pairs.iloc[0,1]
    cum, zscore = backtest_pair(data[t1], data[t2])
    plt.figure(figsize=(10,4))
    cum.plot(title=f"Pairs backtest {t1} vs {t2}")
    plt.savefig(f"{REPORTS}/pairs_backtest_{t1}_{t2}.png", bbox_inches="tight")
    print("Saved backtest plot.")

if __name__=="__main__":
    main()