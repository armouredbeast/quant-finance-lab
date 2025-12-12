import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

TICKER = "AAPL"
START = "2015-01-01"

df = yf.download(TICKER, start=START, progress=False)
df["Return"] = df["Close"].pct_change()
df["Target"] = (df["Return"].shift(-1) > 0).astype(int)

df["MA10"] = df["Close"].rolling(10).mean()
df["MA50"] = df["Close"].rolling(50).mean()
df["Vol"] = df["Return"].rolling(10).std()

df = df.dropna()

X = df[["MA10", "MA50", "Vol"]]
y = df["Target"]

X_train, X_test, y_train, y_test = train_test_split(X, y, shuffle=False)

model = RandomForestClassifier(n_estimators=200, random_state=42)
model.fit(X_train, y_train)

pred = model.predict(X_test)
print(classification_report(y_test, pred))

plt.figure(figsize=(12,4))
plt.plot(df.index[-len(pred):], pred, label="Predicted Direction")
plt.title("Random Forest Return Direction")
plt.show()