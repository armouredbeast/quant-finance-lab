import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

def black_scholes(S, K, T, r, sigma):
    d1 = (np.log(S/K) + (r + 0.5*sigma**2)*T) / (sigma*np.sqrt(T))
    d2 = d1 - sigma*np.sqrt(T)

    call = S*norm.cdf(d1) - K*np.exp(-r*T)*norm.cdf(d2)
    put = K*np.exp(-r*T)*norm.cdf(-d2) - S*norm.cdf(-d1)

    delta = norm.cdf(d1)
    gamma = norm.pdf(d1)/(S*sigma*np.sqrt(T))
    vega = S*norm.pdf(d1)*np.sqrt(T)

    return call, put, delta, gamma, vega

S = np.linspace(50,150,100)
call, _, delta, _, _ = black_scholes(S, 100, 1, 0.05, 0.2)

plt.plot(S, call, label="Call Price")
plt.plot(S, delta, label="Delta")
plt.legend()
plt.title("Black-Scholes Price & Delta")
plt.show()