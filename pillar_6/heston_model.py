import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)

S0, v0 = 100, 0.04
kappa, theta, sigma = 2, 0.04, 0.3
rho, T, N = -0.7, 1, 1000
dt = T/N

S = np.zeros(N)
v = np.zeros(N)
S[0], v[0] = S0, v0

for t in range(1,N):
    z1, z2 = np.random.randn(), np.random.randn()
    z2 = rho*z1 + np.sqrt(1-rho**2)*z2

    v[t] = np.abs(v[t-1] + kappa*(theta-v[t-1])*dt + sigma*np.sqrt(v[t-1]*dt)*z2)
    S[t] = S[t-1]*np.exp(-0.5*v[t]*dt + np.sqrt(v[t]*dt)*z1)

plt.plot(S)
plt.title("Heston Price Path")
plt.show()