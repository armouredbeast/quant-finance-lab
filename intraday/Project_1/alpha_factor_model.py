"""
Alpha Factor Model (single-file)
- Downloads close prices
- Builds simple factors (momentum, volatility)
- Ranks assets cross-sectionally each month
- Forms equal-weight long (top tercile) / short (bottom tercile)
- Computes daily returns and basic performance metrics + plot
"""
import os
import numpy as np
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

TICKERS = ["AAPL","MSFT","GOOGL","AMZN","TSLA"]
START = "2022-01-01"
END = None  # None -> up to today
OUTPUT = "reports"
os.makedirs(OUTPUT, exist_ok=True)

def download_close(tickers):
    data = {}
    for t in tickers:
        df = yf.download(t, start=START, end=END, progress=False)
        data[t] = df['Close']
    prices = pd.concat(data, axis=1)
    prices.columns = tickers
    return prices.dropna(how='all')

def compute_factors(prices):
    # momentum: past 60 trading days return
    mom = prices.pct_change(60).shift(1)
    # volatility: past 60-day std
    vol = prices.pct_change().rolling(60).std().shift(1)
    return mom, vol

def rank_and_construct(prices, mom):
    # resample monthly: on last business day of month
    rets = prices.pct_change().dropna()
    monthly_idx = prices.resample('M').last().index
    positions = pd.DataFrame(index=rets.index, columns=prices.columns).fillna(0.0)
    for dt in monthly_idx:
        if dt not in mom.index: continue
        mo = mom.loc[dt]
        ranks = mo.rank(ascending=False)  # higher = better
        top = ranks <= len(ranks)/3
        bottom = ranks >= 2*len(ranks)/3
        pos = pd.Series(0.0, index=prices.columns)
        if top.sum()>0:
            pos[top.index[top]] = 1.0/top.sum()
        if bottom.sum()>0:
            pos[bottom.index[bottom]] = -1.0/bottom.sum()
        # fill positions until next month
        next_idx = rets.index[rets.index>dt]
        if len(next_idx)==0: break
        next_dt = next_idx[0]
        # apply until next month change
        mask = (rets.index>dt) & (rets.index<= (dt + pd.tseries.offsets.MonthEnd(1)))
        positions.loc[mask, :] = pos.values
    positions = positions.fillna(method='ffill').fillna(0.0)
    return positions

def backtest(positions, prices):
    rets = prices.pct_change().fillna(0)
    strat_rets = (positions.shift(1) * rets).sum(axis=1)
    cum = (1+strat_rets).cumprod()
    return strat_rets, cum

def metrics(series):
    ann_ret = series.mean() * 252
    ann_vol = series.std() * np.sqrt(252)
    sharpe = ann_ret / ann_vol if ann_vol>0 else 0.0
    return ann_ret, ann_vol, sharpe

def main():
    prices = download_close(TICKERS)
    mom, vol = compute_factors(prices)
    positions = rank_and_construct(prices, mom)
    strat_rets, cum = backtest(positions, prices)
    ann_ret, ann_vol, sharpe = metrics(strat_rets)
    print("Ann Ret:", round(ann_ret,4),"Vol:",round(ann_vol,4),"Sharpe:",round(sharpe,4))
    plt.figure(figsize=(10,5))
    plt.plot(cum.index, cum.values)
    plt.title("Alpha Factor Model — Cumulative Value (start=1.0)")
    plt.grid(True)
    plt.savefig(os.path.join(OUTPUT,"alpha_cum.png"))
    print("Saved:", os.path.join(OUTPUT,"alpha_cum.png"))

if __name__=="__main__":
    main()