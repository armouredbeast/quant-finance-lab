#!/usr/bin/env python3
"""
kalman_filter.py
Simple Kalman filter to track time-varying beta between asset returns and market.
Usage: python kalman_filter.py
Outputs: reports/kalman_beta.png
"""
import os, warnings
warnings.filterwarnings("ignore")

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf

REPORTS = "reports"
os.makedirs(REPORTS, exist_ok=True)

def fetch_returns(tickers=["AAPL","^GSPC"], start="2018-01-01"):
    df = yf.download(tickers, start=start, progress=False)["Close"].dropna()
    returns = df.pct_change().dropna()
    return returns

def run_kalman(Y, X, R=1e-5, Q=1e-5):
    """
    Kalman filter for linear regression Y_t = beta_t * X_t + eps
    State is beta_t (scalar) — simple 1D Kalman.
    """
    n = len(Y)
    beta = np.zeros(n)
    P = np.zeros(n)
    beta_prior = 0.0
    P_prior = 1.0
    for t in range(n):
        # predict
        beta_pred = beta_prior
        P_pred = P_prior + Q
        # observation
        xt = X[t]
        yt = Y[t]
        # Kalman gain
        S = xt * P_pred * xt + R
        K = (P_pred * xt) / S
        # update
        beta_upd = beta_pred + K * (yt - xt * beta_pred)
        P_upd = (1 - K * xt) * P_pred
        beta[t] = beta_upd
        P[t] = P_upd
        beta_prior = beta_upd
        P_prior = P_upd
    return beta, P

def main():
    returns = fetch_returns()
    y = returns["AAPL"].values
    x = returns["^GSPC"].values
    beta, P = run_kalman(y, x, R=1e-6, Q=1e-5)
    dates = returns.index
    plt.figure(figsize=(10,4))
    plt.plot(dates, beta, label="beta_kalman")
    plt.title("Time-varying beta (Kalman)")
    plt.legend()
    fn = f"{REPORTS}/kalman_beta.png"
    plt.savefig(fn, bbox_inches="tight")
    print("Saved:", fn)

if __name__=="__main__":
    main()