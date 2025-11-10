import matplotlib.pyplot as plt
import numpy as np
import os

def plot_results(results, frontier_df, output_path="reports/efficient_frontier.png"):

    """
    Plots the efficient frontier and highlights the max Sharpe and min variance portfolios.
    """
    # Normalize column names to lowercase for safety
    frontier_df.columns = [c.lower() for c in frontier_df.columns]
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    plt.figure(figsize=(10, 6))
    plt.scatter(frontier_df['volatility'], frontier_df['return'],
                c=frontier_df['sharpe'], cmap='viridis', alpha=0.6)
    plt.colorbar(label='Sharpe Ratio')

    # Highlight special points
    plt.scatter(results['max_sharpe']['volatility'], results['max_sharpe']['return'],
                color='r', marker='*', s=200, label='Max Sharpe')
    plt.scatter(results['min_var']['volatility'], results['min_var']['return'],
                color='b', marker='X', s=150, label='Min Variance')

    plt.title("Efficient Frontier — Portfolio Optimization")
    plt.xlabel("Volatility (Risk)")
    plt.ylabel("Expected Return")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()
    print(f"✅ Efficient frontier plot saved at: {output_path}")


def plot_portfolio_weights(optimal, output_path="reports/portfolio_weights.png"):
    """
    Visualizes the weight allocation of an optimized portfolio.
    """
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    weights = optimal['weights']
    plt.figure(figsize=(8, 5))
    plt.bar(weights.keys(), weights.values(), color='teal', alpha=0.7)
    plt.title("Optimal Portfolio Weights (Max Sharpe)")
    plt.ylabel("Weight")
    plt.grid(axis='y', linestyle='--', alpha=0.6)
    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()
    print(f"✅ Portfolio weights plot saved at: {output_path}")