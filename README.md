# Neural Network From Scratch (NumPy)

This project implements a **feedforward neural network from first principles** using only NumPy.

No PyTorch.  
No TensorFlow.  
No autograd.

The objective is **mathematical transparency and engineering clarity**, not benchmark performance.

---

## 🎯 What this project demonstrates

- Forward propagation using matrix operations
- Backpropagation derived directly from the chain rule
- Gradient descent optimization
- Modular neural network design
- Clean experiment separation
- Proper Python package structure

This repository is intended to show **understanding**, not abstraction.

---

## 📂 Project Structure
quant_nn/
│
├── src/
│   ├── layers.py          # Linear (dense) layer
│   ├── activations.py     # ReLU activation
│   ├── loss.py            # Mean Squared Error
│   └── network.py         # Forward/backward orchestration
│
├── data/
│   └── synthetic_data.py  # Reproducible toy datasets
│
├── experiments/
│   └── run_experiment.py  # Training experiments
│
├── README.md
├── requirements.txt
└── math.md

---

## 🧠 Model Architecture

For the default experiment:
Input (2)
↓
Linear (2 → 32)
↓
ReLU
↓
Linear (32 → 1)

Loss function:
- Mean Squared Error (MSE)

Optimizer:
- Vanilla Gradient Descent (SGD-style)

---

## ▶️ How to Run

### 1. Create virtual environment (optional but recommended)

```bash
python3 -m venv venv
source venv/bin/activate

pip install -r requirements.txt

python -m experiments.run_experiment


### 📈 Expected Output

You should see the loss decrease over epochs:
epoch=0     loss ≈ 10+
epoch=300   loss ↓
epoch=1000  loss significantly lower


---

# 📄 `requirements.txt`

Keep this **minimal**. That’s a signal.

```text
numpy>=1.26