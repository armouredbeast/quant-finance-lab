# src/activations.py

import numpy as np


class ReLU:
    def __init__(self):
        self.z = None

    def forward(self, z):
        """
        Forward pass
        z: pre-activation input
        """
        self.z = z
        return np.maximum(0, z)

    def backward(self, da):
        """
        Backward pass
        da: gradient from next layer
        """
        dz = da * (self.z > 0)
        return dz