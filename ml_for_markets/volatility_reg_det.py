import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Dense, Input

df = yf.download("AAPL", start="2015-01-01", progress=False)
df["Vol"] = df["Close"].pct_change().rolling(20).std()
vol = df["Vol"].dropna().values.reshape(-1,1)

inp = Input(shape=(1,))
encoded = Dense(8, activation="relu")(inp)
decoded = Dense(1)(encoded)

autoencoder = Model(inp, decoded)
autoencoder.compile(optimizer="adam", loss="mse")
autoencoder.fit(vol, vol, epochs=20, verbose=0)

recon = autoencoder.predict(vol)
error = np.abs(vol - recon)

plt.figure(figsize=(12,4))
plt.plot(error)
plt.title("Autoencoder Reconstruction Error (Regime Signal)")
plt.show()