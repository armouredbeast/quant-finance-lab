import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

tickers = ["AAPL","MSFT","GOOGL","AMZN"]
prices = yf.download(tickers, start="2015-01-01", progress=False)["Close"]

returns = prices.pct_change().dropna()
scaled = StandardScaler().fit_transform(returns)

pca = PCA(n_components=2)
factors = pca.fit_transform(scaled)

plt.figure(figsize=(10,4))
plt.plot(factors[:,0], label="Factor 1")
plt.plot(factors[:,1], label="Factor 2")
plt.title("ML-Driven Latent Factors (PCA)")
plt.legend()
plt.show()