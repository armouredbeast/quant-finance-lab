import numpy as np
import matplotlib.pyplot as plt

def GBM(S0=100, mu=0.05, sigma=0.2, T=1, N=1000):
    dt = T/N
    W = np.cumsum(np.sqrt(dt) * np.random.randn(N))
    t = np.linspace(0, T, N)
    S = S0 * np.exp((mu - 0.5 * sigma**2)*t + sigma * W)

    plt.plot(t, S)
    plt.title("Geometric Brownian Motion")
    plt.show()

    return S

if __name__ == "__main__":
    GBM()