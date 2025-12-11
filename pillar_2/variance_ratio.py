#!/usr/bin/env python3
"""
variance_ratio.py
Implements a simple Lo-MacKinlay variance ratio test for random walk vs mean-reversion.
Usage: python variance_ratio.py
Outputs: reports/vr_results.csv
"""
import os, warnings
warnings.filterwarnings("ignore")

import numpy as np
import pandas as pd
import yfinance as yf
from scipy.stats import norm

REPORTS = "reports"
os.makedirs(REPORTS, exist_ok=True)

def fetch_returns(ticker="AAPL", start="2015-01-01"):
    df = yf.download(ticker, start=start, progress=False)["Close"].dropna()
    r = df.pct_change().dropna()
    return r

def variance_ratio_test(r, q=2):
    """
    Lo-MacKinlay variance ratio test for aggregation q.
    r : pandas Series of returns
    q : aggregation horizon
    returns dict with vr statistic and z-stat
    """
    r = r.values.flatten()
    n = len(r)
    mu = r.mean()
    m = n - q + 1
    # aggregated return variance
    var_r = r.var(ddof=1)
    # variance of q-period returns
    agg = np.array([r[i:i+q].sum() for i in range(m)])
    var_agg = agg.var(ddof=1)
    vr = var_agg / (var_r * q)
    # asymptotic z statistic (Lo & MacKinlay, heteroskedasticity-robust omitted for brevity)
    z = (vr - 1) * np.sqrt(n * (q - 1) / (2.0 * q))
    pvalue = 2 * (1 - norm.cdf(abs(z)))
    return {"q": q, "vr": vr, "z": z, "pvalue": pvalue}

def main():
    ticker = "AAPL"
    r = fetch_returns(ticker)
    results = []
    for q in [2,5,10,20]:
        res = variance_ratio_test(r, q=q)
        res["ticker"] = ticker
        results.append(res)
        print(res)
    pd.DataFrame(results).to_csv(f"{REPORTS}/vr_results_{ticker}.csv", index=False)
    print("Saved VR results.")

if __name__=="__main__":
    main()