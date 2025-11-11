Policy-Search Portfolio Agent (toy)
-----------------------------------
Purpose: lightweight policy-search optimizer to find static weights optimizing Sharpe on historical data.

Usage:
  pip install pandas numpy yfinance matplotlib
  python policy_search_portfolio.py

Output:
  - reports/policy_search_cum.png

Notes:
  - Not production RL. Replace with policy-gradient / PPO with stable-baselines for real RL.