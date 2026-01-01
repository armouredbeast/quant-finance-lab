from src.layers import Linear
from src.activations import ReLU
from src.loss import MSELoss
from src.network import NeuralNetwork

import numpy as np


def generate_data(n_samples=1000):
    """
    Synthetic regression dataset
    y = 3x1 - 2x2 + noise
    """
    X = np.random.randn(2, n_samples)
    noise = 0.1 * np.random.randn(1, n_samples)
    y = 3 * X[0:1, :] - 2 * X[1:2, :] + noise
    return X, y


def run_experiment(
    hidden_units=32,
    lr=0.01,
    epochs=1500
):
    X, y = generate_data()

    model = NeuralNetwork([
        Linear(2, hidden_units),
        ReLU(),
        Linear(hidden_units, 1)
    ])

    loss_fn = MSELoss()

    for epoch in range(epochs):
        # Forward
        y_pred = model.forward(X)

        # Loss
        loss = loss_fn.forward(y_pred, y)

        # Backward
        grad = loss_fn.backward()
        model.backward(grad)

        # Update (SGD inside layers)
        model.update(lr)

        if epoch % 100 == 0:
            print(
                f"[hidden={hidden_units}, lr={lr}] "
                f"epoch={epoch}, loss={loss:.6f}"
            )


if __name__ == "__main__":
    run_experiment()