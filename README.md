# Quant Research Laboratory

![License](https://img.shields.io/badge/License-MIT-brightgreen.svg)
![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![Status](https://img.shields.io/badge/Open%20Source-Yes-black.svg)

> Open-source quantitative research, portfolio models, and algorithmic trading strategy prototypes.
> Built for learning, experimentation and thought leadership in systematic finance.

---

## ⚠️ Legal Notice (Read Before Using)

This repository is **strictly for educational and research purposes.**

- No investment or trading advice is being provided.
- Code examples are experimental research prototypes.
- Use at your own risk — you are responsible for your decisions.

By using this repo, you agree to assume full responsibility for any outcomes.

---

## 📘 Repository Structure
quant-finance-lab/
│
├── portfolio_models/            ← Long-term investing / portfolio theory
│     ├── 01_Portfolio_Optimization/
│     ├── 02_CVaR_Funding_Optimization/
│     ├── 03_Liquidity_Capital_Model/
│     ├── 04_Multi_Factor_Risk_Model/
│     ├── 05_Regime_Detection_Model/
│
├── intraday_strategies/         ← Execution / intraday / trading systems
│     ├── 06_Market_Condition_Screener.py
│     ├── 07_MeanReversion_5-Min.py
│     ├── 08_Momentum_Breakout.py
│     ├── 09_Backtester_Slippage.py
│     ├── 10_SmartOrder_Execution.py
│     ├── 11_FeatureDriven_SignalModel.py
│     ├── 12_PolicySearch_Portfolio.py
│
├── reports/                     ← Generated charts & result exports
└── README.md
---

## ✅ Project Index (All 12 Included)

| No. | Project Name | Domain | What It Demonstrates |
|-----|-------------|---------|---------------------|
| **01** | Portfolio Optimization (Markowitz) | Portfolio Theory | Efficient frontier & optimal weights |
| **02** | CVaR Funding Optimization | Risk Management | Conditional VaR optimization |
| **03** | Liquidity & Capital Model | Capital Efficiency | Turnover cost vs performance |
| **04** | Multi-Factor Risk Model (PCA) | Systematic Alpha | Risk factor decomposition |
| **05** | Regime Detection (HMM) | Market Regimes | Bull / Bear detection using HMM |
| **06** | Market Condition Screener | Intraday Trading | Detect trending / ranging environments |
| **07** | Intraday Mean Reversion (5-min) | Intraday Trading | RSI/VWAP reversion signals |
| **08** | Intraday Momentum Breakout | Intraday Trading | Volume + price trend continuation |
| **09** | Backtester with Slippage & Costs | Execution | Execution cost modeling |
| **10** | Smart Order Routing (Weight Optimization) | Execution | Allocation across multiple assets |
| **11** | Feature-Driven ML Signal Model | ML + Trading | ML signals from engineered features |
| **12** | Portfolio Policy Search (RL-inspired) | Portfolio Allocation | Adaptive policy weight optimization |

---

## ▶️ Running a Model

Inside repo root:

```sh
python3 intraday_strategies/07_MeanReversion_5-Min.py

python3 -m venv venv
source venv/bin/activate     # macOS / Linux
venv\Scripts\activate        # Windows
pip install -r requirements.txt

## 
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
