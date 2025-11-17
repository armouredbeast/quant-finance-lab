"""
PILLAR 1 — PROJECT 3
Distribution Explorer (PDF + CDF Visualizer)
Author: Quant Research Laboratory

Plots:
- Empirical PDF (or PMF)
- CDF
For discrete and continuous distributions.
"""

import numpy as np
import matplotlib.pyplot as plt
from collections import Counter
from scipy.stats import norm


# -------------------------------------------------------
# Helper plotting functions
# -------------------------------------------------------

def plot_discrete_distribution(samples, title):
    counts = Counter(samples)
    x = np.array(sorted(counts.keys()))
    pmf = np.array([counts[k] / len(samples) for k in x])
    cdf = np.cumsum(pmf)

    plt.figure(figsize=(10, 4))

    # PMF
    plt.subplot(1, 2, 1)
    plt.bar(x, pmf, color="steelblue")
    plt.title(f"{title} – PMF")
    plt.xlabel("Value")
    plt.ylabel("Probability")

    # CDF
    plt.subplot(1, 2, 2)
    plt.step(x, cdf, where="post", color="darkred")
    plt.title(f"{title} – CDF")
    plt.xlabel("Value")
    plt.ylabel("Cumulative Probability")

    plt.tight_layout()
    plt.show()


def plot_continuous_distribution(samples, title, bins=60):
    samples = np.array(samples)
    sorted_x = np.sort(samples)
    cdf = np.arange(1, len(samples) + 1) / len(samples)

    plt.figure(figsize=(10, 4))

    # PDF (histogram density)
    plt.subplot(1, 2, 1)
    plt.hist(samples, bins=bins, density=True, alpha=0.7, color="steelblue")
    plt.title(f"{title} – PDF")
    plt.xlabel("Value")
    plt.ylabel("Density")

    # CDF
    plt.subplot(1, 2, 2)
    plt.plot(sorted_x, cdf, color="darkred")
    plt.title(f"{title} – CDF")
    plt.xlabel("Value")
    plt.ylabel("Cumulative Probability")

    plt.tight_layout()
    plt.show()


# -------------------------------------------------------
# GENERATORS
# -------------------------------------------------------

def generate_discrete():
    return {
        "Bernoulli (p=0.3)": np.random.binomial(1, 0.3, 5000),
        "Binomial (n=10, p=0.5)": np.random.binomial(10, 0.5, 5000),
        "Poisson (lambda=3)": np.random.poisson(3, 5000),
    }


def generate_continuous():
    return {
        "Uniform(0,1)": np.random.uniform(0, 1, 5000),
        "Exponential(lambda=1.5)": np.random.exponential(1 / 1.5, 5000),
        "Normal(0,1)": np.random.normal(0, 1, 5000),
    }


# -------------------------------------------------------
# MAIN
# -------------------------------------------------------

if __name__ == "__main__":
    print("=== DISTRIBUTION EXPLORER ===\n")

    # Discrete
    discrete = generate_discrete()
    for name, samples in discrete.items():
        print(f"Plotting {name} ...")
        plot_discrete_distribution(samples, name)

    # Continuous
    continuous = generate_continuous()
    for name, samples in continuous.items():
        print(f"Plotting {name} ...")
        plot_continuous_distribution(samples, name)