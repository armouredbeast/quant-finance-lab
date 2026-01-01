# Mathematical Foundations of the Neural Network

This document derives the equations implemented in the codebase.

---

## 1. Problem Definition

Given a dataset:

\[
\mathcal{D} = \{(x^{(i)}, y^{(i)})\}_{i=1}^{N}
\]

where:
- \( x \in \mathbb{R}^d \)
- \( y \in \mathbb{R} \)

We aim to learn a function:

\[
\hat{y} = f(x; \theta)
\]

by minimizing a loss function.

---

## 2. Linear Layer (Affine Transformation)

For layer \( l \):

\[
z^{(l)} = W^{(l)} a^{(l-1)} + b^{(l)}
\]

where:
- \( W^{(l)} \in \mathbb{R}^{n_l \times n_{l-1}} \)
- \( b^{(l)} \in \mathbb{R}^{n_l} \)

---

## 3. Activation Function (ReLU)

\[
a^{(l)} = \max(0, z^{(l)})
\]

Derivative:

\[
\frac{\partial a^{(l)}}{\partial z^{(l)}} =
\begin{cases}
1 & z^{(l)} > 0 \\
0 & z^{(l)} \le 0
\end{cases}
\]

---

## 4. Loss Function (Mean Squared Error)

\[
\mathcal{L} = \frac{1}{N} \sum_{i=1}^{N} (\hat{y}^{(i)} - y^{(i)})^2
\]

Derivative w.r.t prediction:

\[
\frac{\partial \mathcal{L}}{\partial \hat{y}} =
\frac{2}{N} (\hat{y} - y)
\]

---

## 5. Backpropagation

### Output Layer

Since the output layer is linear:

\[
\delta^{(L)} = \frac{\partial \mathcal{L}}{\partial z^{(L)}} =
\frac{2}{N} (\hat{y} - y)
\]

---

### Hidden Layers

Using the chain rule:

\[
\delta^{(l)} =
\left(W^{(l+1)T} \delta^{(l+1)}\right)
\odot g'(z^{(l)})
\]

---

## 6. Gradients

\[
\frac{\partial \mathcal{L}}{\partial W^{(l)}} =
\delta^{(l)} a^{(l-1)T}
\]

\[
\frac{\partial \mathcal{L}}{\partial b^{(l)}} =
\delta^{(l)}
\]

---

## 7. Parameter Update (Gradient Descent)

\[
W := W - \eta \frac{\partial \mathcal{L}}{\partial W}
\]

\[
b := b - \eta \frac{\partial \mathcal{L}}{\partial b}
\]

---

## 8. Summary

This implementation directly mirrors these equations in code.

No automatic differentiation is used.

Correctness is validated by observing monotonic loss reduction during training.