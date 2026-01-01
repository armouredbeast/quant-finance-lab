# src/layers.py

import numpy as np


class Linear:
    def __init__(self, in_features, out_features):
        """
        Fully connected (dense) layer
        """
        # He initialization (good for ReLU)
        self.W = np.random.randn(out_features, in_features) * np.sqrt(2.0 / in_features)
        self.b = np.zeros((out_features, 1))

        # Cache for backprop
        self.x = None

        # Gradients
        self.dW = None
        self.db = None

    def forward(self, x):
        """
        Forward pass
        x: shape (in_features, batch_size)
        """
        self.x = x
        z = self.W @ x + self.b
        return z

    def backward(self, dz):
        """
        Backward pass
        dz: gradient from next layer (out_features, batch_size)
        """
        batch_size = self.x.shape[1]

        # Gradients
        self.dW = (dz @ self.x.T) / batch_size
        self.db = np.sum(dz, axis=1, keepdims=True) / batch_size

        # Gradient w.r.t input
        dx = self.W.T @ dz
        return dx

    def update(self, lr):
        """
        Gradient descent update
        """
        self.W -= lr * self.dW
        self.b -= lr * self.db