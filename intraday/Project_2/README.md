Risk Parity + Vol Target
------------------------
Purpose: low-complexity risk-parity and vol-targeting example.

How to run:
  pip install pandas numpy yfinance matplotlib
  python risk_parity_vol_target.py

Output:
  - reports/risk_parity_cum.png
Notes:
  - This uses inverse-vol weighting as a risk-parity proxy; not constrained optimization.