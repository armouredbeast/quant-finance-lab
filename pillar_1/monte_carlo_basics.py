import numpy as np
import matplotlib.pyplot as plt

def monte_carlo_pi(n=100000):
    x = np.random.rand(n)
    y = np.random.rand(n)
    inside = (x**2 + y**2) <= 1
    pi_est = 4 * np.mean(inside)

    plt.scatter(x[inside], y[inside], s=1, alpha=0.5)
    plt.scatter(x[~inside], y[~inside], s=1, alpha=0.5)
    plt.title(f"Monte Carlo π Estimate: {pi_est}")
    plt.show()

    return pi_est

if __name__ == "__main__":
    print(monte_carlo_pi())