import numpy as np
import matplotlib.pyplot as plt

def brownian_motion(T=1, N=1000):
    dt = T/N
    increments = np.sqrt(dt) * np.random.randn(N)
    W = np.cumsum(increments)

    plt.plot(np.linspace(0, T, N), W)
    plt.title("Brownian Motion Sample Path")
    plt.show()

    return W

if __name__ == "__main__":
    brownian_motion()