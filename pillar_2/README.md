📈 Pillar 2 — Time-Series & Statistical Modelling

A structured suite of quantitative models for forecasting, regime detection, volatility modelling, and statistical structure discovery in financial time series.

This module focuses on building production-grade statistical engines used across quant research, market modelling, and algorithmic trading desks. Each project progressively deepens your understanding of autocorrelation structure, volatility clustering, market regimes, and price dynamics under uncertainty.

⸻

## 📦 Project Overview

⸻

1️⃣ ARIMA / AR / MA Auto-Selector

A smart model-selection utility that:
	•	Performs automatic stationarity checks (ADF, KPSS)
	•	Identifies best (p, d, q) using AIC/BIC
	•	Benchmarks AR, MA, ARIMA, ARMA
	•	Generates forecasts with confidence intervals
	•	Visualizes fitted vs actual series + residual diagnostics

Applications:
Market forecasting, macro time-series modelling, risk factor evolution.

⸻

2️⃣ GARCH Volatility Forecaster

A complete volatility-modelling engine:
	•	Fits GARCH, EGARCH, GJR-GARCH models
	•	Computes conditional variance forecasts
	•	Captures volatility clusters + leverage effects
	•	Extracts long-run volatility, persistence metrics
	•	Includes returns preprocessing + diagnostics

Applications:
Options risk, VaR forecasts, intraday leverage targeting, volatility surfaces.

⸻

3️⃣ Regime Switching Model (Hidden Markov Model — Advanced)

A full HMM-based market regime classifier:
	•	Detects bull/bear/sideways structural regimes
	•	Learns state transition probabilities
	•	Produces smoothed state sequences
	•	Supports Gaussian & Student-t emissions
	•	Visualizes regime overlays on price series

Applications:
Regime-aware portfolio allocation, switching strategies, macro timing.

⸻

4️⃣ Cointegration & Pairs Trading Engine

A complete market-neutral alpha module:
	•	Performs Engle-Granger & Johansen cointegration
	•	Computes hedge ratios + residual spread
	•	Detects mean-reversion opportunities
	•	Generates entry/exit signals
	•	Includes full backtesting loop

Applications:
Stat arb, HFT spread trades, long-short market-neutral portfolios.

⸻

5️⃣ Kalman Filter Price Tracker

A robust state-space filtering engine:
	•	Smooths noisy price observations
	•	Estimates hidden “true price” + trend
	•	Online updating capability
	•	Supports multi-dimensional states
	•	Includes prediction & update step plots

Applications:
Execution algorithms, signal smoothing, intraday fair-value estimation.

⸻

6️⃣ Variance Ratio Test (Random Walk Detection)

A statistical test module for checking market efficiency:
	•	Performs Lo–MacKinlay Variance Ratio Test
	•	Supports homoskedastic & heteroskedastic variants
	•	Computes VR statistics across multiple horizons
	•	Classifies series as random walk / mean-reverting / trending

Applications:
Market behaviour diagnostics, model selection, pretesting for ARIMA/GARCH.

⸻

## 🎯 Learning Outcomes

By completing Pillar 2, you will:
✔ Understand and model time-dependent structure in returns
✔ Master volatility modelling & clustering frameworks
✔ Detect & classify structural market regimes
✔ Evaluate price series for predictability vs randomness
✔ Build full statistical engines just like sell-side quant teams do

⸻
