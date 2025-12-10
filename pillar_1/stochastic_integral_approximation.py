import numpy as np

def stochastic_integral(N=10000):
    dt = 1/N
    W = np.cumsum(np.sqrt(dt) * np.random.randn(N))
    integrand = np.sin(np.linspace(0, 1, N))
    integral = np.sum(integrand * np.diff(np.insert(W, 0, 0)))

    print("∫ sin(t) dW_t ≈", integral)
    return integral

if __name__ == "__main__":
    stochastic_integral()