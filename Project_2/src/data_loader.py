import yfinance as yf
import pandas as pd

class DataLoader:
    def __init__(self, tickers, start="2022-01-01", end=None, interval="1d"):
        if isinstance(tickers, str):
            tickers = [tickers]
        self.tickers = tickers
        self.start = start
        self.end = end
        self.interval = interval

    def fetch_data(self):
        data = {}
        for t in self.tickers:
            print(f"Fetching data for {t}...")
            df = yf.download(t, start=self.start, end=self.end, interval=self.interval)
            data[t] = df
        return data