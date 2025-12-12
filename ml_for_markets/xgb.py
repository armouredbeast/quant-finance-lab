import yfinance as yf
import pandas as pd
import xgboost as xgb
import matplotlib.pyplot as plt

df = yf.download("AAPL", start="2015-01-01", progress=False)
df["Return"] = df["Close"].pct_change()
df["MA20"] = df["Close"].rolling(20).mean()
df["MA50"] = df["Close"].rolling(50).mean()
df["Vol"] = df["Return"].rolling(20).std()
df["Target"] = (df["Return"].shift(-1) > 0).astype(int)
df = df.dropna()

X = df[["MA20", "MA50", "Vol"]]
y = df["Target"]

model = xgb.XGBClassifier(n_estimators=200, max_depth=3)
model.fit(X, y)

xgb.plot_importance(model)
plt.title("XGBoost Feature Importance")
plt.show()