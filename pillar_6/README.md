📌 PILLAR 6 — Derivatives Pricing & Advanced Models

This pillar focuses on derivatives pricing under uncertainty, combining stochastic calculus, numerical methods, and risk-aware modeling.
The goal is not just pricing instruments, but understanding model behavior, assumptions, and limitations — exactly how these models are used on volatility, exotics, and structured products desks.

⸻

🔹 Models Covered

1️⃣ Black–Scholes Pricer + Greeks Engine

Concepts
	•	Lognormal asset dynamics
	•	Risk-neutral valuation
	•	Sensitivities (Greeks)

Why it matters
	•	Industry baseline for options pricing
	•	Greeks are central to hedging and risk management
	•	Benchmark for validating more complex models

Output
	•	Call price vs underlying
	•	Delta sensitivity visualization

⸻

2️⃣ Binomial Tree Pricer

Concepts
	•	Discrete-time approximation of stochastic processes
	•	Convergence to Black–Scholes
	•	Early exercise intuition

Why it matters
	•	Transparent pricing framework
	•	Used for American options and validation checks
	•	Highlights numerical stability and step-size effects

Output
	•	Option price convergence as tree depth increases

⸻

3️⃣ Heston Stochastic Volatility Model

Concepts
	•	Mean-reverting variance process
	•	Correlated Brownian motions
	•	Volatility smile generation

Why it matters
	•	Addresses constant-volatility limitation of Black–Scholes
	•	Widely used on equity volatility desks
	•	Foundation for volatility surface modeling

Output
	•	Simulated asset price path with stochastic volatility

⸻

4️⃣ Stochastic Volatility Calibration Tool

Concepts
	•	Realized volatility estimation
	•	Rolling-window variance
	•	Market-observed volatility dynamics

Why it matters
	•	Calibration bridges theory and market data
	•	Highlights regime changes and clustering
	•	Used in model fitting and risk diagnostics

Output
	•	Realized volatility time series from market data

⸻

5️⃣ Merton Jump-Diffusion Model

Concepts
	•	Poisson jump processes
	•	Fat tails and discontinuous price moves
	•	Crash and event risk modeling

Why it matters
	•	Captures sudden market shocks
	•	Used in stress testing and tail-risk pricing
	•	Complements continuous diffusion models

Output
	•	Price path showing jump behavior

⸻

6️⃣ Exotic Option Pricer (Barrier Options)

Concepts
	•	Path-dependent payoffs
	•	Knock-in / knock-out conditions
	•	Monte Carlo simulation

Why it matters
	•	Exotics dominate structured products
	•	Path-dependence introduces nonlinear risk
	•	Monte Carlo is the industry standard for complex payoffs

Output
	•	Monte Carlo estimated exotic option price

⸻

🔹 Design Philosophy
	•	No hardcoded data — live or simulated inputs only
	•	Visualization-first to build intuition
	•	Minimal abstractions to keep math transparent
	•	Interview-ready code: readable, explainable, extensible

⸻

🔹 Skills Demonstrated
	•	Risk-neutral pricing
	•	Stochastic calculus intuition
	•	Numerical methods (Monte Carlo, trees)
	•	Volatility modeling
	•	Tail-risk awareness
	•	Model limitations & assumptions

⸻

🔹 How This Is Used in Practice

These models directly map to:
	•	Equity volatility trading desks
	•	Exotic derivatives pricing
	•	Model validation & benchmarking
	•	Risk management and stress testing
	•	Structured products design

The same framework extends naturally to:
	•	Calibration engines
	•	Volatility surfaces
	•	Multi-asset models
	•	Real-time risk systems

⸻

📍 Positioning

This pillar represents advanced quant competency, bridging:
	•	Mathematical rigor
	•	Market intuition
	•	Production-aware modeling

It is designed to complement earlier pillars (probability, time-series, portfolios, ML) and prepare for real trading and structuring environments.
