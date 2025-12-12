import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
from sklearn.preprocessing import MinMaxScaler

df = yf.download("AAPL", start="2015-01-01", progress=False)[["Close"]]

scaler = MinMaxScaler()
scaled = scaler.fit_transform(df)

X, y = [], []
for i in range(60, len(scaled)):
    X.append(scaled[i-60:i])
    y.append(scaled[i])

X, y = np.array(X), np.array(y)

model = Sequential([
    LSTM(50, return_sequences=True, input_shape=(60,1)),
    LSTM(50),
    Dense(1)
])

model.compile(optimizer="adam", loss="mse")
model.fit(X, y, epochs=5, batch_size=32, verbose=0)

pred = model.predict(X)

plt.figure(figsize=(12,5))
plt.plot(scaler.inverse_transform(y), label="Actual")
plt.plot(scaler.inverse_transform(pred), label="Predicted")
plt.title("LSTM Price Prediction")
plt.legend()
plt.show()