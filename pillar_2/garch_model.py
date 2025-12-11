#!/usr/bin/env python3
"""
garch_model.py
Simple GARCH(1,1) estimation & volatility forecast using 'arch' package.
Usage: python garch_model.py
Outputs: reports/garch_params.csv, reports/garch_vol_forecast.png
"""
import os, warnings
warnings.filterwarnings("ignore")

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf
from arch import arch_model

REPORTS = "reports"
os.makedirs(REPORTS, exist_ok=True)

def fetch_returns(ticker="AAPL", start="2018-01-01"):
    df = yf.download(ticker, start=start, progress=False)
    close = df["Close"].dropna()
    returns = 100 * close.pct_change().dropna()  # percent returns
    return returns

def fit_garch(returns):
    am = arch_model(returns, vol="Garch", p=1, q=1, mean="AR", lags=1, dist="normal")
    res = am.fit(disp="off")
    return res

def forecast_vol(res, horizon=20):
    f = res.forecast(horizon=horizon, reindex=False)
    # conditional volatility (annualization omitted)
    mean_vol = np.sqrt(f.variance.values[-1])
    return mean_vol

def main():
    ticker = "AAPL"
    returns = fetch_returns(ticker)
    print("Data length:", len(returns))

    print("Fitting GARCH(1,1)...")
    res = fit_garch(returns)
    print(res.summary())

    params = res.params
    pd.DataFrame(params).to_csv(f"{REPORTS}/garch_params_{ticker}.csv")

    vol_fore = forecast_vol(res, horizon=30)
    plt.figure(figsize=(10,4))
    plt.plot(res.conditional_volatility[-250:], label="cond_vol")
    plt.title(f"GARCH cond vol recent - {ticker}")
    plt.legend()
    plt.savefig(f"{REPORTS}/garch_vol_{ticker}.png", bbox_inches="tight")
    print("Saved vol plot and params.")

if __name__=="__main__":
    main()