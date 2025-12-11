#!/usr/bin/env python3
"""
arima_auto.py
Auto-select AR / MA / ARMA / ARIMA model by grid + pmdarima.auto_arima fallback.
Usage: python arima_auto.py
Outputs: reports/arima_summary.csv, reports/arima_forecast.png
"""
import os
import warnings
warnings.filterwarnings("ignore")

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf
from statsmodels.tsa.stattools import adfuller
from pmdarima import auto_arima
from statsmodels.tsa.arima.model import ARIMA

REPORTS = "reports"
os.makedirs(REPORTS, exist_ok=True)

def fetch_close(ticker="^GSPC", start="2018-01-01", end=None):
    df = yf.download(ticker, start=start, end=end, progress=False)
    return df["Close"].dropna()

def test_stationarity(series):
    res = adfuller(series, maxlag=10, autolag="AIC")
    return {"adf_stat": res[0], "pvalue": res[1], "usedlag": res[2]}

def fit_auto_arima(series):
    m = auto_arima(series, seasonal=False, stepwise=True, suppress_warnings=True,
                   error_action="ignore", max_order=6)
    return m

def fit_and_forecast(series, n_forecast=30):
    model = ARIMA(series, order=(1,0,1)).fit()
    fc = model.get_forecast(steps=n_forecast)
    mean = fc.predicted_mean
    ci = fc.conf_int()
    return model, mean, ci

def main():
    ticker = "AAPL"
    print("Downloading:", ticker)
    series = fetch_close(ticker)
    series = series.asfreq("B").fillna(method="ffill")
    print("Length:", len(series))

    print("ADF test...")
    adf = test_stationarity(series.diff().dropna())  # usually diff for prices
    print(adf)

    print("Running auto_arima...")
    arima = fit_auto_arima(series)
    print("Selected order:", arima.order)

    print("Fitting ARIMA (p,d,q) from auto_arima...")
    p,d,q = arima.order
    model = ARIMA(series, order=(p,d,q)).fit()
    print(model.summary().tables[1])

    n_forecast = 30
    fc = model.get_forecast(steps=n_forecast)
    mean = fc.predicted_mean
    ci = fc.conf_int()

    plt.figure(figsize=(10,5))
    series[-300:].plot(label="history")
    mean.plot(label="forecast")
    plt.fill_between(mean.index, ci.iloc[:,0], ci.iloc[:,1], alpha=0.2)
    plt.legend()
    plt.title(f"ARIMA({p},{d},{q}) forecast for {ticker}")
    fn = f"{REPORTS}/arima_forecast_{ticker}.png"
    plt.savefig(fn, bbox_inches="tight")
    print("Saved:", fn)

    summary = {
        "ticker": ticker,
        "n": len(series),
        "adf_pvalue": adf["pvalue"],
        "order": str((p,d,q))
    }
    pd.DataFrame([summary]).to_csv(f"{REPORTS}/arima_summary.csv", index=False)
    print("Done.")

if __name__ == "__main__":
    main()