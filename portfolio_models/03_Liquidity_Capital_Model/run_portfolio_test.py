from src.data_loader import DataLoader
from src.portfolio import PortfolioOptimizer
from src.visualize import plot_results, plot_portfolio_weights
import pandas as pd

# Step 1: Load Market Data
loader = DataLoader(["AAPL", "MSFT", "GOOGL"], start="2022-01-01")
data = loader.fetch_data()

# Step 2: Prepare Daily Returns
prices = pd.concat([data[t]['Close'] for t in data], axis=1)
prices.columns = data.keys()
returns = prices.pct_change().dropna()

# Step 3: Run Optimization
optimizer = PortfolioOptimizer(returns)
results = optimizer.optimize()              # Contains both max Sharpe & min variance
frontier_df = optimizer.efficient_frontier()  # Efficient frontier curve

# Step 4: Print Key Results
print("📊 Optimal Portfolios:\n")
print("MAX SHARPE:")
print(results['max_sharpe'], "\n")
print("MIN VARIANCE:")
print(results['min_var'])

# Step 5: Plot and Save Charts
plot_results(results, frontier_df)
plot_portfolio_weights(results['max_sharpe'], output_path="reports/portfolio_weights.png")