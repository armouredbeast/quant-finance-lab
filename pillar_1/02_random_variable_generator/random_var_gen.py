"""
PILLAR 1 — PROJECT 2
Random Variable Generator
Author: Quant Research Laboratory

Description:
A clean toolkit for generating discrete and continuous random variables.
Includes:
- Bernoulli
- Binomial
- Poisson
- Uniform
- Exponential
- Normal
"""

import numpy as np
from collections import Counter
import math
import matplotlib.pyplot as plt


# -------------------------------------------------------
# DISCRETE RANDOM VARIABLES
# -------------------------------------------------------

def bernoulli(p: float, n: int = 10000):
    """Generate Bernoulli(p)."""
    samples = np.random.rand(n) < p
    return samples.astype(int)


def binomial(n_trials: int, p: float, n: int = 10000):
    """Generate Binomial(n_trials, p)."""
    return np.random.binomial(n_trials, p, n)


def poisson(lmbda: float, n: int = 10000):
    """Generate Poisson(lambda)."""
    return np.random.poisson(lmbda, n)


# -------------------------------------------------------
# CONTINUOUS RANDOM VARIABLES
# -------------------------------------------------------

def uniform(a: float, b: float, n: int = 10000):
    return np.random.uniform(a, b, n)


def exponential(lmbda: float, n: int = 10000):
    return np.random.exponential(1 / lmbda, n)


def normal(mu: float, sigma: float, n: int = 10000):
    return np.random.normal(mu, sigma, n)


# -------------------------------------------------------
# EMPIRICAL VISUALIZER
# -------------------------------------------------------

def plot_discrete(samples, title):
    counts = Counter(samples)
    x, y = zip(*sorted(counts.items()))
    plt.figure(figsize=(6, 3))
    plt.bar(x, np.array(y) / len(samples))
    plt.title(title)
    plt.xlabel("Value")
    plt.ylabel("Empirical Probability")
    plt.tight_layout()
    plt.show()


def plot_continuous(samples, title, bins=50):
    plt.figure(figsize=(6, 3))
    plt.hist(samples, bins=bins, density=True, alpha=0.7)
    plt.title(title)
    plt.xlabel("Value")
    plt.ylabel("Density")
    plt.tight_layout()
    plt.show()


# -------------------------------------------------------
# DEMO
# -------------------------------------------------------

if __name__ == "__main__":
    print("\n=== Bernoulli(p=0.3) ===")
    b = bernoulli(p=0.3)
    print("Empirical mean:", np.mean(b))
    plot_discrete(b, "Bernoulli(p=0.3)")

    print("\n=== Binomial(n=10, p=0.4) ===")
    bn = binomial(10, 0.4)
    print("Empirical mean:", np.mean(bn))
    plot_discrete(bn, "Binomial(10, 0.4)")

    print("\n=== Poisson(lambda=3) ===")
    ps = poisson(3)
    print("Empirical mean:", np.mean(ps))
    plot_discrete(ps, "Poisson(3)")

    print("\n=== Uniform(0,1) ===")
    uf = uniform(0, 1)
    print("Empirical mean:", np.mean(uf))
    plot_continuous(uf, "Uniform(0,1)")

    print("\n=== Exponential(lambda=1.5) ===")
    ex = exponential(1.5)
    print("Empirical mean:", np.mean(ex))
    plot_continuous(ex, "Exponential(1.5)")

    print("\n=== Normal(μ=0, σ=1) ===")
    nm = normal(0, 1)
    print("Empirical mean:", np.mean(nm))
    plot_continuous(nm, "Normal(0,1)")