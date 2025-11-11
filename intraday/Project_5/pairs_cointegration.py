"""
Pairs trading via cointegration:
- Downloads two series
- Tests OLS cointegration (engle-granger) via regression residuals and ADF
- Creates z-score on spread and mean-reversion entry/exit
"""
import os
import numpy as np
import pandas as pd
import yfinance as yf
from statsmodels.tsa.stattools import adfuller
import statsmodels.api as sm
import matplotlib.pyplot as plt

TICKER_X="AAPL"
TICKER_Y="MSFT"
START="2022-01-01"
OUTPUT="reports"
os.makedirs(OUTPUT, exist_ok=True)

def download(x,y):
    dx=yf.download([x,y], start=START, progress=False)['Close'].dropna()
    return dx[x], dx[y]

def test_cointegration(x,y):
    # regress y = a + b*x
    x2 = sm.add_constant(x)
    res = sm.OLS(y, x2).fit()
    spread = y - res.predict(x2)
    adf = adfuller(spread)
    return res, spread, adf

def backtest(spread, z_entry=1.5, z_exit=0.5):
    z = (spread - spread.mean())/spread.std()
    position = np.where(z > z_entry, -1, np.where(z < -z_entry, 1, 0))
    # exit rules
    for i in range(1,len(position)):
        if position[i]==0 and abs(z[i])<z_exit:
            position[i]=0
    # assume equal notional, pnl ~ -position * spread_change
    pnl = -position * spread.diff().fillna(0)
    equity=(1+pnl).cumprod()
    return z, position, pnl, equity

def main():
    x,y = download(TICKER_X, TICKER_Y)
    res, spread, adf = test_cointegration(x,y)
    print("ADF stat:", adf[0], "p-value:", adf[1])
    z, pos, pnl, eq = backtest(spread)
    plt.figure(figsize=(10,5))
    plt.plot(eq)
    plt.title("Pairs Trading Equity Curve")
    plt.grid(True)
    plt.savefig(os.path.join(OUTPUT,"pairs_eq.png"))
    print("Saved:", os.path.join(OUTPUT,"pairs_eq.png"))

if __name__=="__main__":
    main()