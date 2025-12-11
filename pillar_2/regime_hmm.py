#!/usr/bin/env python3
"""
regime_hmm.py
Hidden Markov Model regime detection (Gaussian emissions) using hmmlearn.
Usage: python regime_hmm.py
Outputs: reports/regime_states.csv and reports/regime_plot.png
"""
import os, warnings
warnings.filterwarnings("ignore")

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf
from hmmlearn.hmm import GaussianHMM

REPORTS = "reports"
os.makedirs(REPORTS, exist_ok=True)

def fetch_returns(tickers, start="2019-01-01"):
    df = yf.download(tickers, start=start, progress=False)["Close"].dropna()
    returns = df.pct_change().dropna()
    return returns

def fit_hmm(returns, n_states=2):
    model = GaussianHMM(n_components=n_states, covariance_type="full", n_iter=200, random_state=42)
    model.fit(returns.values)
    hidden_states = model.predict(returns.values)
    return model, hidden_states

def plot_states(dates, price_series, states, out="reports/regime_plot.png"):
    plt.figure(figsize=(12,5))
    plt.plot(dates, price_series, label="Price")
    for s in np.unique(states):
        mask = states == s
        plt.scatter(dates[mask], price_series[mask], s=8, label=f"State {s}")
    plt.legend()
    plt.title("Regime states overlay")
    plt.savefig(out, bbox_inches="tight")
    print("Saved:", out)

def main():
    tickers = ["^GSPC", "AAPL"]
    returns = fetch_returns(tickers)
    # use market (index) returns only for regime detection
    market = returns["^GSPC"].values.reshape(-1,1)
    print("Fitting HMM...")
    model, states = fit_hmm(market, n_states=2)
    dates = returns.index
    # save states
    df = pd.DataFrame({"date": dates, "state": states})
    df.to_csv(f"{REPORTS}/regime_states.csv", index=False)
    print("Saved regime states.")
    # plot with index price
    price = yf.download("^GSPC", start=dates[0], progress=False)["Close"].dropna()
    plot_states(price.index, price.values, states)
    print("Done.")

if __name__=="__main__":
    main()