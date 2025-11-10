# utils.py
import matplotlib.pyplot as plt
import seaborn as sns
import os
import pandas as pd

def plot_regime_states(dates, prices, states, asset="^GSPC"):
    os.makedirs("reports", exist_ok=True)
    plt.figure(figsize=(12,6))
    for s in range(states.max() + 1):
        mask = states == s
        plt.plot(dates[mask], prices[asset][mask], ".", label=f"Regime {s}")
    plt.title(f"Regime Detection for {asset}")
    plt.legend()
    plt.savefig("reports/regime_detection.png", dpi=300)
    plt.close()

def summarize_regimes(returns, states):
    df = pd.DataFrame({"Regime": states, "Return": returns.flatten()})
    summary = df.groupby("Regime")["Return"].agg(["mean", "std", "count"])
    print("\n=== Regime Summary ===")
    print(summary)
    return summary