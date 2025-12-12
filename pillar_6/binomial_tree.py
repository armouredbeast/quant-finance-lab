import numpy as np
import matplotlib.pyplot as plt

def binomial_call(S, K, r, T, sigma, N):
    dt = T/N
    u = np.exp(sigma*np.sqrt(dt))
    d = 1/u
    p = (np.exp(r*dt)-d)/(u-d)

    prices = np.array([S*(u**j)*(d**(N-j)) for j in range(N+1)])
    values = np.maximum(prices-K,0)

    for i in range(N):
        values = np.exp(-r*dt)*(p*values[1:]+(1-p)*values[:-1])

    return values[0]

Ns = range(5,200)
prices = [binomial_call(100,100,0.05,1,0.2,n) for n in Ns]

plt.plot(Ns, prices)
plt.title("Binomial Tree Convergence")
plt.xlabel("Steps")
plt.ylabel("Option Price")
plt.show()