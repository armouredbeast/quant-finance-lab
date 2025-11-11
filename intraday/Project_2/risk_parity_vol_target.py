"""
Risk Parity + Vol Target (single-file)
- Computes inverse-volatility weights (risk parity approximation)
- Vol targeting to target_vol annualized
- Backtests simple daily returns
"""
import os, math
import numpy as np
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

TICKERS=["AAPL","MSFT","GOOGL"]
START="2022-01-01"
OUTPUT="reports"
TARGET_VOL=0.12
os.makedirs(OUTPUT, exist_ok=True)

def download_close(tickers):
    data={}
    for t in tickers:
        df=yf.download(t,start=START,progress=False)
        data[t]=df['Close']
    prices=pd.concat(data,axis=1).dropna()
    prices.columns=tickers
    return prices

def inv_vol_weights(returns, window=60):
    vol = returns.rolling(window).std().iloc[-1]
    iv = 1.0 / (vol + 1e-9)
    w = iv / iv.sum()
    return w

def apply_vol_target(weights, returns, target=TARGET_VOL):
    port_ret = (returns * weights).sum(axis=1)
    hist_vol = port_ret.rolling(60).std() * np.sqrt(252)
    scale = target / (hist_vol + 1e-9)
    scale = scale.shift(1).fillna(1.0).clip(0.0,5.0)
    scaled = port_ret * scale
    return scaled, scale

def main():
    prices = download_close(TICKERS)
    rets = prices.pct_change().dropna()
    w = inv_vol_weights(rets)
    print("Weights (risk-parity approx):", {k:round(v,4) for k,v in zip(TICKERS,w)})
    strat_rets, scale = apply_vol_target(w, rets)
    cum=(1+strat_rets).cumprod()
    ann_ret = strat_rets.mean()*252
    ann_vol = strat_rets.std()*np.sqrt(252)
    print("AnnRet",round(ann_ret,4),"AnnVol",round(ann_vol,4))
    plt.figure(figsize=(10,5))
    plt.plot(cum)
    plt.title("Risk-Parity + Vol Target — Cumulative")
    plt.grid(True)
    plt.savefig(os.path.join(OUTPUT,"risk_parity_cum.png"))
    print("Saved:", os.path.join(OUTPUT,"risk_parity_cum.png"))

if __name__=="__main__":
    main()