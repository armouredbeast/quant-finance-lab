"""
PILLAR 1 — PROJECT 4
Law of Large Numbers (LLN) Simulator
Author: Quant Research Laboratory

Visualizes sample mean convergence for:
- Normal(0,1)
- Uniform(0,1)
- Exponential(lambda=1)
"""

import numpy as np
import matplotlib.pyplot as plt


# -------------------------------------------------------
# RUNNING MEAN FUNCTION
# -------------------------------------------------------

def running_mean(samples):
    return np.cumsum(samples) / np.arange(1, len(samples) + 1)


# -------------------------------------------------------
# PLOTTER
# -------------------------------------------------------

def plot_lln(samples, true_mean, title):
    rm = running_mean(samples)

    plt.figure(figsize=(10, 5))
    plt.plot(rm, label="Running Mean", linewidth=1.3)
    plt.axhline(true_mean, color='red', linestyle='--', label=f"True Mean = {true_mean}")

    plt.title(f"LLN Convergence — {title}")
    plt.xlabel("Number of Samples")
    plt.ylabel("Running Mean")
    plt.legend()
    plt.grid(alpha=0.3)
    plt.tight_layout()
    plt.show()


# -------------------------------------------------------
# MAIN
# -------------------------------------------------------

if __name__ == "__main__":
    print("=== LLN Simulator ===\n")

    N = 20000  # Large enough to clearly show convergence

    # ---------------------------------------------------
    # Normal Distribution
    # ---------------------------------------------------
    norm_samples = np.random.normal(0, 1, N)
    print("Plotting Normal(0,1) LLN...")
    plot_lln(norm_samples, true_mean=0, title="Normal(0,1)")

    # ---------------------------------------------------
    # Uniform Distribution
    # ---------------------------------------------------
    uni_samples = np.random.uniform(0, 1, N)
    print("Plotting Uniform(0,1) LLN...")
    plot_lln(uni_samples, true_mean=0.5, title="Uniform(0,1)")

    # ---------------------------------------------------
    # Exponential Distribution
    # ---------------------------------------------------
    exp_samples = np.random.exponential(1, N)  # mean = 1
    print("Plotting Exponential(λ=1) LLN...")
    plot_lln(exp_samples, true_mean=1, title="Exponential(λ=1)")