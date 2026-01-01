# src/network.py

class NeuralNetwork:
    def __init__(self, layers):
        """
        layers: list of layers and activations in order
        Example:
        [
            Linear(2, 16),
            ReLU(),
            Linear(16, 1)
        ]
        """
        self.layers = layers

    def forward(self, x):
        """
        Forward pass through all layers
        """
        for layer in self.layers:
            x = layer.forward(x)
        return x

    def backward(self, grad):
        """
        Backward pass through all layers (reverse order)
        """
        for layer in reversed(self.layers):
            grad = layer.backward(grad)
        return grad

    def update(self, lr):
        """
        Update parameters for layers that have them
        """
        for layer in self.layers:
            if hasattr(layer, "update"):
                layer.update(lr)