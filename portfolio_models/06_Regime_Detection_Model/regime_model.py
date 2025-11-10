import numpy as np
import pandas as pd
from sklearn.mixture import GaussianMixture
from codescripts.data_loader import DataLoader
from codescripts.utils import plot_regime_states

# ==============================
# CONFIG
# ==============================
TICKERS = ["^GSPC", "AAPL", "MSFT"]
START_DATE = "2020-01-01"
END_DATE = "2024-12-31"
FREQ = "1d"                      # daily
N_STATES = 3                     # Hidden Markov Regimes

# ==============================
# MAIN PIPELINE
# ==============================

if __name__ == "__main__":

    print("\n===== Regime Detection Model (HMM) =====\n")

    # Load prices
    loader = DataLoader(TICKERS, START_DATE, END_DATE, interval=FREQ)
    prices = loader.fetch_data()                          # dataframe of prices

    # Compute returns
    returns = loader.compute_returns(prices)

    # Extract market returns (just benchmark index)
    market_returns = returns["^GSPC"].values.reshape(-1, 1)

    # Hidden Markov Model / Gaussian Mixture
    hmm_model = GaussianMixture(
        n_components=N_STATES,
        covariance_type="full",
        random_state=42
    )
    hmm_model.fit(market_returns)

    # Predict market regimes
    states = hmm_model.predict(market_returns)

    # ✅ FIX shape mismatch — remove first date from prices
    prices = prices.iloc[1:]

    # ==============================
    # SAVE REPORT
    # ==============================
    out = pd.DataFrame({
        "Date": prices.index,
        "Market_Returns": market_returns.flatten(),
        "Regime": states
    })
    out.to_csv("./reports/regime_states.csv", index=False)

    print("✅ Regime states saved to: ./reports/regime_states.csv")

    # Plot the regimes
    plot_regime_states(prices.index, prices, states, asset="^GSPC")

    print("\n✅ Plot generated")