# Quant Research Laboratory

![License](https://img.shields.io/badge/License-MIT-brightgreen.svg)
![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![Status](https://img.shields.io/badge/Open%20Source-Yes-black.svg)

> Open-source quantitative research, portfolio models, and algorithmic trading strategy prototypes.
> Built for learning, experimentation and thought leadership in systematic finance.

---

⚠️ Legal & Usage Disclaimer

This repository is provided strictly for educational and research purposes.
	•	No investment advice is provided.
	•	No trading recommendations are made.
	•	All code is experimental and illustrative.
	•	Users assume full responsibility for any usage or outcomes.

This code is not production-ready trading software.

⸻

📁 Repository Structure

quant-finance-lab/
│
├── pillar_1/           # Probability & Mathematical Foundations
├── pillar_2/           # Time-Series & Statistical Modeling
├── portfolio_models/   # Portfolio Theory & Risk Models
├── intraday/           # Intraday & Algorithmic Trading Systems
├── ml_for_markets/     # Machine Learning for Financial Markets
├── pillar_6/           # Derivatives Pricing & Advanced Models
│
├── requirements.txt
├── .gitignore
└── README.md

---

Each folder contains self-contained projects with code and documentation.

⸻

🧱 Pillar Overview

🔹 Pillar 1 — Probability & Mathematical Foundations

Folder: pillar_1/

Focus:
	•	Probability theory
	•	Random variables & distributions
	•	Monte Carlo simulation
	•	Law of Large Numbers & CLT
	•	Stochastic processes (Random Walk, Brownian Motion)
	•	Markov chains & martingales

Purpose:

Build mathematical intuition required for all downstream quant models.

⸻

🔹 Pillar 2 — Time-Series & Statistical Modeling

Folder: pillar_2/

Projects include:
	•	AR / MA / ARIMA model selection
	•	GARCH volatility forecasting
	•	Hidden Markov regime switching
	•	Cointegration & pairs trading
	•	Kalman filtering
	•	Variance ratio testing

Purpose:

Model temporal dependence, volatility dynamics, and regime behavior.

⸻

🔹 Portfolio Models — Portfolio Theory & Risk

Folder: portfolio_models/

Projects include:
	1.	Markowitz Efficient Frontier Optimizer
	2.	CVaR & Tail-Risk Minimizer
	3.	Liquidity-Adjusted Portfolio Optimizer
	4.	Dynamic Backtesting & Signal Engine
	5.	Multi-Factor Risk Model (Fama-French + custom factors)
	6.	Regime-Aware Portfolio Allocator

Purpose:

Institutional portfolio construction, risk decomposition, and allocation logic.

⸻

🔹 Intraday — Algorithmic Trading & Execution

Folder: intraday/

Projects include:
	•	SMA crossover strategies
	•	Momentum & RSI intraday systems
	•	Slippage-adjusted backtesting
	•	Volatility-targeted strategies
	•	Policy search–based allocation models

Purpose:

Understand execution, microstructure effects, and intraday risk.

⸻

🔹 Pillar 5 — Machine Learning for Markets

Folder: ml_for_markets/

Projects include:
	•	Random Forest return classification
	•	XGBoost feature importance
	•	LSTM price prediction
	•	Autoencoder volatility regime detection
	•	SHAP-based model explainability
	•	ML-driven factor construction (PCA + ML)

Purpose:

Apply ML as a modeling tool, not a black box.

⸻

🔹 Pillar 6 — Derivatives Pricing & Advanced Models

Folder: pillar_6/

Projects include:
	•	Black-Scholes pricer + Greeks
	•	Binomial tree pricer
	•	Heston stochastic volatility model
	•	Stochastic volatility calibration
	•	Merton jump-diffusion
	•	Exotic option pricing (Barrier / Asian)

Purpose:

Pricing, volatility modeling, and risk under uncertainty.

⸻

▶️ Running a Project
	1.	Create a virtual environment:
	python3 -m venv venv
source venv/bin/activate   # macOS / Linux
venv\Scripts\activate      # Windows
	2.	Install dependencies:
	pip install -r requirements.txt
	3.	Run any project:
	python pillar_1/probability_simulator.py
python intraday/slippage_adjusted_backtester.py
python pillar_6/black_scholes_pricer.py
---
Most scripts:
	•	Download market data automatically
	•	Plot results directly
	•	Do not write files unless explicitly stated

⸻

🧠 Design Philosophy
	•	One concept → one model
	•	Readable > clever
	•	Math first, code second
	•	Plots for intuition
	•	Minimal dependencies

This repository is meant to be:
	•	Interview-explainable
	•	Research-oriented
	•	Easy to extend

⸻

🌱 Project Goals
	•	Build deep quantitative intuition through implementation
	•	Bridge theory and real-world financial modeling
	•	Create a transparent, open research archive
	•	Serve as a long-term quant research notebook
""" 
🌱 Goal of This Repository
	•	To learn quant finance by building, testing, and validating ideas.
	•	To make complex quant models simple, reproducible, and open-source.
	•	To create a portfolio-quality collection of research projects.

  📡 Connect

🔗 LinkedIn Company Page
Quant Research Laboratory


MIT License

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the “Software”), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""



## ▶️ Running a Model

Inside repo root:

```sh
python3 intraday_strategies/07_MeanReversion_5-Min.py

python3 -m venv venv
source venv/bin/activate     # macOS / Linux
venv\Scripts\activate        # Windows
pip install -r requirements.txt


Large files/data should remain gitignored.

---

### 🔧 Setup

```bash
pip install -r requirements.txt
python script_name.py
