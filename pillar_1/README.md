🚀 Pillar 1 — Probability & Stochastic Foundations

Quant Research Laboratory — Core Mathematical Models

This collection of projects forms the foundation of the Quant Research Laboratory.
Each model is designed to build intuition for probability, stochastic processes, Monte Carlo methods, and the mathematical engines used in quantitative finance.

These 12 projects act as the mathematical scaffolding for all higher-level models (time-series, derivatives, portfolio risk, and machine learning).

⸻

📂 Project Index (Pillar 1A + 1B)

⸻

1. Probability Simulator (Coins / Dice / Bayes)

Simulates discrete events (coin flips, dice rolls) and demonstrates Bayes’ updating.
Helps build intuition for conditional probability and event space reasoning.

⸻

2. Random Variable Generator

Generates samples from several discrete probability distributions.
Useful for understanding pmf, expected value, and variance.

⸻

3. Distribution Explorer (PDF / CDF)

Interactive exploration of normal, exponential, uniform, gamma and more.
Plots PDF, CDF, and overlays statistical moments for intuition.

⸻

4. Law of Large Numbers (LLN) Simulator

Monte-Carlo engine demonstrating empirical mean → true mean convergence.
Shows how sample averages stabilize with increasing N.

⸻

5. Central Limit Theorem (CLT) Engine

Samples from arbitrary distributions and visualizes the CLT in action.
Shows how the distribution of sample means → Gaussian, regardless of base distribution.

⸻

6. Monte Carlo Basics (Detailed)

General-purpose Monte Carlo simulation framework.
Covers random draws, expectation approximations, and convergence diagnostics.

⸻

7. Brownian Motion Generator

Simulates standard Wiener process paths.
Builds intuition for diffusion, variance scaling, and continuous-time randomness.

⸻

8. Stochastic Integral Approximation

Numerically approximates integrals of the form:
\int_0^T f(t, W_t)\, dW_t
Using Riemann sums, Itô interpretation, and discrete Brownian paths.
Core foundation for derivatives pricing and SDE modeling.

⸻

9. Markov Chain Simulator

Constructs finite-state Markov chains, transition matrices, and multi-step evolution.
Includes stationary distribution and ergodicity tests.

⸻

10. Geometric Brownian Motion (GBM)

Implements the SDE:
dS_t = \mu S_t\, dt + \sigma S_t\, dW_t
Generates asset price paths used in Black-Scholes, option pricing, and risk simulations.

⸻

11. Martingale Examples

Demonstrates martingale processes such as fair games, compensated Poisson processes, and discounted asset prices under risk-neutral measure.

⸻

12. Stochastic Process Toolkit (Random Walks, Basic SDEs)

A compact set of utilities for simulating:
	•	discrete random walks
	•	drift-diffusion models
	•	mean-reverting processes (Ornstein-Uhlenbeck)

This forms the bridge toward full stochastic calculus and quantitative modeling.

⸻

🎯 Purpose of Pillar 1

These projects are designed to:
	•	Build deep intuition behind every mathematical assumption used in quant finance
	•	Prepare for derivatives pricing, risk modeling, and algo-trading strategies
	•	Serve as standalone educational modules for aspiring quants
	•	Provide reusable tools for future model development in Pillars 2–6

⸻

📌 How to Use This Repository

Each project is self-contained with:
	•	project_name.py
	•	Clear explanations inside code
	•	Visualizations where applicable
	•	Reproducible simulation settings

⸻

📈 Next Steps

Once Pillar 1 is complete, the roadmap continues with:
	•	Pillar 2: Time-Series & Statistical Models
	•	Pillar 3: Portfolio Theory & Risk
	•	Pillar 4: Algorithmic Trading
	•	Pillar 5: Machine Learning for Markets
	•	Pillar 6: Derivatives Pricing

This layered structure ensures mastery from fundamentals → advanced execution.

⸻

If you want, I can also generate:

✅ A professional cover README for the entire repo
✅ Separate README files inside each folder
✅ Auto-generated project badges
✅ A contributor-style architecture diagram
