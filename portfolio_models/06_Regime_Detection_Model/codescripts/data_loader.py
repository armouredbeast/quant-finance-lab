# codescripts/data_loader.py

import yfinance as yf
import pandas as pd

class DataLoader:
    def __init__(self, tickers, start, end=None, interval="1d"):
        self.tickers = tickers
        self.start = start
        self.end = end
        self.interval = interval

    def fetch_data(self):
        close_prices = {}

        for t in self.tickers:
            print(f"Fetching data for {t} ...")

            df = yf.download(
                t,
                start=self.start,
                end=self.end,
                interval=self.interval,
                progress=False,
                auto_adjust=True
            )

            if df is None or df.empty:
                print(f"⚠️  No data returned for {t} — skipping.")
                continue

            # ✅ Ensure 'Close' becomes a Series with a proper index
            series = pd.Series(df["Close"].values.ravel(), index=df.index, name=t)
            close_prices[t] = series

        if len(close_prices) == 0:
            raise ValueError("❌ No ticker returned valid data. Check tickers/date range/internet.")

        # ✅ Convert dict of Series → DataFrame (safe)
        df_all = pd.concat(close_prices, axis=1)

        # Clean dataset
        df_all.dropna(inplace=True)

        return df_all

    def compute_returns(self, prices_df):
        if prices_df is None or prices_df.empty:
            print("❌ No price data available to compute returns.")
            return None

        returns = prices_df.pct_change().dropna()
        return returns  # <-- this was missing