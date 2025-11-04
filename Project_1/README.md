Portfolio Optimization (Quant Research Series)
----------------------------------------------------------------------
--> Overview

        * This project implements an industry-grade portfolio optimization 
          engine based on Modern Portfolio Theory (Markowitz).
        * It computes the efficient frontier, maximum Sharpe ratio, 
          and minimum variance portfolios using real-time market data (via Yahoo Finance).
----------------------------------------------------------------------

--> Motivation

    * Portfolio construction is a foundational task in asset management.
    * This project replicates the first stage of a front-office quant desk —
      constructing optimal portfolios under risk–return trade-offs.

----------------------------------------------------------------------

--> Core Concepts
	•	Mean–Variance Optimization
	•	Sharpe Ratio Maximization
	•	Efficient Frontier Construction
	•	Annualized Returns & Risk Calculation

---------------------------------------------------------------------

-->Key Results
    * Max Sharpe Portfolio  == Sharpe ≈ 0.65
    * Expected Annual Return  == ~17.9%
    * Volatility  == ~25.6%
    * Optimal Weights  ==  AAPL 32%, MSFT 38%, GOOGL 30%

----------------------------------------------------------------------

--> Future Extensions
	•	Add dynamic rebalancing module
	•	Integrate transaction costs
	•	Extend to multi-asset optimization (FX, commodities)
----------------------------------------------------------------------

--> Plots:
	•	reports/efficient_frontier.png
	•	reports/portfolio_weights.png
