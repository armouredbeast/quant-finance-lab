# Project 5 — CLT Engine

Demonstrates the Central Limit Theorem with visual examples across multiple parent distributions.

**How to run**

**What to inspect**
- As `n` grows, the histogram of sample means becomes more Gaussian.
- Empirical standard deviation of sample means ≈ `sigma / sqrt(n)` (theory).
- Highly skewed parents (e.g., chi-square) still converge to normal for large `n`.

**Outputs**
- `reports/clt_<DIST>_n<N>.png` — plots for each distribution and sample size.