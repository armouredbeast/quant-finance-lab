from typing import assert_type

import pandas as pd
import numpy as np
import cvxpy as cp
import matplotlib.pyplot as plt
from fontTools.misc.cython import returns

# Step 1: Generate synthetic return data for 5 assets
np.random.seed(42)
returns = np.random.randn(1000,5)*0.02 ## --> 1000 days, 5 assets
assets = ['AAPL','MSFT','GOOGL', 'AMZN','META']

df = pd.DataFrame(returns, columns = assets)

# Step 2: Compute mean returns and covariance matrix
mean_returns = df.mean()
cov_matrix = df.cov()

# Step 3: Define optimization variables
n = len(assets)
w = cp.Variable(n)

# Step 4: Define objective function (minimize risk)
risk = cp.quad_form(w, cov_matrix.values)
expected_return = mean_returns.values @ w

# Step 5: constraints - sum of weights = 1 , each weight >=0
constraints = [cp.sum(w)==1,w>=0]

# Step 6 : Optimization problem — minimize risk for a given return
target_return = 0.0005 # target daily return
prob = cp.Problem(cp.Minimize(risk),constraints + [expected_return>= target_return])
prob.solve()

# Step 7: Display optimal weights
opt_weights = w.value
result = pd.DataFrame({'Asset': assets, 'Optimal Weight': opt_weights})

# Step 8: Visualize allocation
plt.bar(assets, opt_weights, color= 'teal')
plt.title('Optimal Portfolio Allocation')
plt.ylabel('Weight')
plt.grid(True)
plt.show()
