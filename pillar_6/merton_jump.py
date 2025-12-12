import numpy as np
import matplotlib.pyplot as plt

S0, mu, sigma = 100, 0.1, 0.2
lam, jump_mu, jump_sigma = 0.3, -0.2, 0.3
T, N = 1, 1000
dt = T/N

S = np.zeros(N)
S[0] = S0

for t in range(1,N):
    jump = np.random.rand() < lam*dt
    J = np.exp(jump_mu + jump_sigma*np.random.randn()) if jump else 1
    S[t] = S[t-1]*np.exp((mu-0.5*sigma**2)*dt + sigma*np.sqrt(dt)*np.random.randn())*J

plt.plot(S)
plt.title("Merton Jump-Diffusion Path")
plt.show()