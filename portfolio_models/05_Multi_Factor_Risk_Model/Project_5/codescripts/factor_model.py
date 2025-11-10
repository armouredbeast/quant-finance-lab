"""
Multi Factor Risk Model
- Downloads price data for a set of tickers(portfolio + factor proxies)
- Builds Returns matrix
- Option A: Run OLS regressions of asseet returns on chosen factors (market, size, momentum proxy)
- Option B: Run PCA to discover latent factors
- Compute:
    * Factor Betas
    * Specific (idiosyncratic) variances
    * Covariance decomposition: Sigma = B Var(F) B' +D
    * Risk contribution per factor for a simple equal-weight portfolio
- Save Plots into ../reports/
"""

import os
import numpy as np
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.decomposition import PCA
import statsmodels.api as sm

# Config/ user inputs
TICKERS = ['AAPL','MSFT','GOOGL']
FACTOR_TICKERS = ['^GSPC','XLK']
START_DATE = '2022-01-01'
END_DATE = None
FREQ = '1d'
RFR = 0.02
OUT_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)),'reports')
os.makedirs(OUT_DIR,exist_ok = True)


# Helper functions

def download_close(tickers,start,end,interval='1d'):
    out = {}
    for t in tickers:
        print(f'Downloaning {t} ...')
        df = yf.download(t, start = start, end = end, interval=interval, progress = False)
        if df.empty:
            raise RuntimeError(f"No data for {t}")
        out[t] = df['Close']
        out[t].name = t
    return pd.concat(out.values(), axis = 1, keys=out.keys())
def compute_returns(price_df):
    return price_df.pct_change().dropna()

# -----------------------------
# 1. Download prices & compute returns
# -----------------------------
all_tickers = list(set(TICKERS + FACTOR_TICKERS))
prices = download_close(all_tickers, START_DATE, END_DATE, interval=FREQ)
prices = prices.loc[:, all_tickers]  # ensure column order
prices.to_csv(os.path.join(OUT_DIR, "prices_snapshot.csv"))

returns = compute_returns(prices)
assets = returns[TICKERS]
factors = returns[FACTOR_TICKERS]

# Align and drop NA
data = pd.concat([assets, factors], axis=1).dropna()
assets = data[TICKERS]
factors = data[FACTOR_TICKERS]

print("Data ranges:", data.index.min(), data.index.max())
print("Assets shape:", assets.shape, "Factors shape:", factors.shape)

# -----------------------------
# 2. Add constant and run OLS regressions asset ~ factors
# -----------------------------
X = sm.add_constant(factors)  # adds intercept
betas = pd.DataFrame(index=X.columns, columns=TICKERS, dtype=float)
resid_vars = pd.Series(index=TICKERS, dtype=float)

for ticker in TICKERS:
    y = assets[ticker]
    model = sm.OLS(y, X).fit()
    betas[ticker] = model.params
    resid_vars[ticker] = model.resid.var(ddof=1)
    print(f"Regression {ticker} done. R2: {model.rsquared:.4f}")

betas = betas.T  # rows: asset, columns: const + factor proxies
betas.index.name = "Asset"

# -----------------------------
# 3. Factor covariance & decomposition
# -----------------------------
factor_returns = factors
factor_cov = factor_returns.cov()   # sample covariance (daily)
# convert to annualized by multiply by trading days (approx 252)
TRADING_DAYS = 252
factor_cov_ann = factor_cov * TRADING_DAYS

# Build B (beta matrix) excluding the constant term
B = betas.drop(columns="const").values  # shape: (n_assets, n_factors)
D = np.diag(resid_vars.values * TRADING_DAYS)  # idiosyncratic variance (annualized)

Sigma_systematic = B @ factor_cov_ann.values @ B.T
Sigma_total = Sigma_systematic + D

# Portfolio example: equal weights
w = np.repeat(1.0 / len(TICKERS), len(TICKERS))
port_var = w.T @ Sigma_total @ w
port_std = np.sqrt(port_var)

# Factor contributions to variance: contribution_k = w' * (B_k * Var(F_k) * B_k') * w
# Simpler: compute marginal contributions
marginal_contrib = (Sigma_total @ w)  # marginal contribution to portfolio variance per asset
contrib_per_asset = w * marginal_contrib
# Factor-level contributions (approx): compute exposures to each factor then their contribution
factor_var = np.diag(factor_cov_ann)  # if factors uncorrelated; for general factors use matrix
# Using matrix form:
factor_contrib_matrix = (w @ B)  # portfolio exposure to each factor
factor_contrib_total = factor_contrib_matrix @ factor_cov_ann.values @ factor_contrib_matrix.T

# -----------------------------
# 4. Outputs to show and save
# -----------------------------
# Betas table (per asset)
betas_out = betas.copy()
betas_out.to_csv(os.path.join(OUT_DIR, "factor_betas.csv"))

# Specific/Idiosyncratic risk
specific_risk = pd.Series(np.sqrt(np.diag(D)), index=TICKERS)
specific_risk.to_csv(os.path.join(OUT_DIR, "specific_risk.csv"))

# Covariance matrices
pd.DataFrame(Sigma_systematic, index=TICKERS, columns=TICKERS).to_csv(os.path.join(OUT_DIR, "sigma_systematic.csv"))
pd.DataFrame(Sigma_total, index=TICKERS, columns=TICKERS).to_csv(os.path.join(OUT_DIR, "sigma_total.csv"))

# Print summary
print("\n=== Summary ===")
print("Portfolio variance (annual):", port_var)
print("Portfolio volatility (annual):", port_std)
print("Factor contribution (total, annual):", factor_contrib_total)
print("Specific risk (annual std):")
print(specific_risk)

# -----------------------------
# 5. Plots: betas, risk decomposition, correlation heatmap
# -----------------------------
sns.set(style="whitegrid")

# Betas bar chart
plt.figure(figsize=(8,4))
betas.drop(columns="const").plot(kind="bar", figsize=(10,4))
plt.title("Factor Betas (per asset)")
plt.ylabel("Beta value")
plt.tight_layout()
plt.savefig(os.path.join(OUT_DIR, "factor_betas.png"), dpi=150)
plt.close()

# Specific risk bar
plt.figure(figsize=(6,4))
sns.barplot(x=specific_risk.index, y=specific_risk.values)
plt.title("Specific (Idiosyncratic) Risk (annual std)")
plt.ylabel("Annualized Std Dev")
plt.tight_layout()
plt.savefig(os.path.join(OUT_DIR, "specific_risk.png"), dpi=150)
plt.close()

# Heatmap of total covariance
plt.figure(figsize=(6,5))
sns.heatmap(pd.DataFrame(Sigma_total, index=TICKERS, columns=TICKERS), annot=True, fmt=".4f")
plt.title("Total Covariance Matrix (annualized)")
plt.tight_layout()
plt.savefig(os.path.join(OUT_DIR, "sigma_total_heatmap.png"), dpi=150)
plt.close()

# Save a small report CSV with high level metrics
report = pd.Series({
    "portfolio_annual_variance": port_var,
    "portfolio_annual_volatility": port_std,
    "factor_contribution_total": factor_contrib_total,
})
report.to_csv(os.path.join(OUT_DIR, "summary_report.csv"))

print(f"\n✅ Reports saved under: {OUT_DIR}")