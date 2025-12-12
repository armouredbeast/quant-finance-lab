import numpy as np
import yfinance as yf
import matplotlib.pyplot as plt

data = yf.download("^GSPC", period="2y")["Close"]
returns = np.log(data/data.shift(1)).dropna()

realized_vol = returns.rolling(21).std()*np.sqrt(252)

plt.plot(realized_vol)
plt.title("Realized Volatility (21d)")
plt.show()