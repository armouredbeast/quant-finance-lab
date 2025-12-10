import numpy as np

def fair_random_walk(N=1000):
    X = np.cumsum(np.random.choice([-1, 1], size=N))
    return X

def discounted_gbm_martingale(S0=100, mu=0.05, sigma=0.2, r=0.05, N=1000):
    dt = 1/N
    W = np.cumsum(np.sqrt(dt) * np.random.randn(N))
    t = np.linspace(0, 1, N)
    S = S0 * np.exp((mu - 0.5*sigma**2)*t + sigma*W)
    discounted = S * np.exp(-r*t)
    return discounted

if __name__ == "__main__":
    print("Random Walk Martingale Example Generated")