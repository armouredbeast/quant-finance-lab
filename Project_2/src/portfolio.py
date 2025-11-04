import numpy as np
import pandas as pd
from scipy.optimize import minimize


class PortfolioOptimizer:
    """
    Portfolio Optimizer for Efficient Frontier Analysis.
    Supports:
        - Maximum Sharpe Ratio Optimization
        - Minimum Variance Portfolio
        - Efficient Frontier Construction
    """

    def __init__(self, returns: pd.DataFrame, risk_free_rate: float = 0.02):
        self.returns = returns
        self.mean_returns = returns.mean()
        self.cov_matrix = returns.cov()
        self.risk_free_rate = risk_free_rate

    # ---------------------------
    #  Core portfolio math
    # ---------------------------
    def portfolio_performance(self, weights: np.ndarray):
        """Calculate portfolio return, volatility, and Sharpe ratio."""
        weights = np.array(weights)
        annual_return = np.sum(self.mean_returns * weights) * 252
        annual_volatility = np.sqrt(
            np.dot(weights.T, np.dot(self.cov_matrix * 252, weights))
        )
        sharpe_ratio = (annual_return - self.risk_free_rate) / annual_volatility
        return annual_return, annual_volatility, sharpe_ratio

    # ---------------------------
    #  Objective functions
    # ---------------------------
    def _neg_sharpe(self, weights):
        """Objective: maximize Sharpe ratio (so minimize negative Sharpe)."""
        return -self.portfolio_performance(weights)[2]

    def _min_volatility(self, weights):
        """Objective: minimize portfolio volatility."""
        return self.portfolio_performance(weights)[1]

    # ---------------------------
    #  Optimization core
    # ---------------------------
    def _optimize(self, objective, bounds=(0, 0.5)):
        """Solve optimization given objective (min vol or max Sharpe)."""
        num_assets = len(self.mean_returns)
        constraints = {'type': 'eq', 'fun': lambda x: np.sum(x) - 1}
        bounds = tuple(bounds for _ in range(num_assets))

        result = minimize(
            objective,
            x0=num_assets * [1.0 / num_assets],
            method='SLSQP',
            bounds=bounds,
            constraints=constraints,
        )
        return result.x

    # ---------------------------
    #  Portfolio Optimization
    # ---------------------------
    def optimize(self):
        """Find maximum Sharpe ratio and minimum variance portfolios."""
        # Max Sharpe
        weights_sharpe = self._optimize(self._neg_sharpe)
        ret_s, vol_s, sharpe_s = self.portfolio_performance(weights_sharpe)

        # Min Variance
        weights_min = self._optimize(self._min_volatility)
        ret_v, vol_v, sharpe_v = self.portfolio_performance(weights_min)

        return {
            "max_sharpe": {
                "weights": dict(zip(self.mean_returns.index, weights_sharpe)),
                "return": ret_s,
                "volatility": vol_s,
                "sharpe": sharpe_s,
            },
            "min_var": {
                "weights": dict(zip(self.mean_returns.index, weights_min)),
                "return": ret_v,
                "volatility": vol_v,
                "sharpe": sharpe_v,
            },
        }

    # ---------------------------
    #  Efficient Frontier
    # ---------------------------
    def efficient_frontier(self, points: int = 50):
        """
        Compute efficient frontier curve between min and max target returns.
        Returns DataFrame with volatility, return, and implied Sharpe ratio.
        """
        num_assets = len(self.mean_returns)
        target_returns = np.linspace(
            self.mean_returns.min() * 252, self.mean_returns.max() * 252, points
        )
        frontier = []

        for target in target_returns:
            constraints = (
                {"type": "eq", "fun": lambda x: np.sum(x) - 1},
                {
                    "type": "eq",
                    "fun": lambda x, t=target: np.sum(self.mean_returns * x) * 252 - t,
                },
            )
            bounds = tuple((0, 0.5) for _ in range(num_assets))

            result = minimize(
                lambda w: np.sqrt(np.dot(w.T, np.dot(self.cov_matrix * 252, w))),
                num_assets * [1.0 / num_assets],
                method="SLSQP",
                bounds=bounds,
                constraints=constraints,
            )

            if result.success:
                vol = np.sqrt(np.dot(result.x.T, np.dot(self.cov_matrix * 252, result.x)))
                sharpe = (target - self.risk_free_rate) / vol
                frontier.append((vol, target, sharpe))

        return pd.DataFrame(frontier, columns=["volatility", "return", "sharpe"])