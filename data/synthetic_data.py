import numpy as np


def linear_regression_data(
    n_samples=1000,
    noise_std=0.1,
    seed=42
):
    """
    Generates synthetic linear regression data:
    y = 3x1 - 2x2 + noise

    Returns:
        X : shape (2, n_samples)
        y : shape (1, n_samples)
    """
    rng = np.random.default_rng(seed)

    X = rng.standard_normal((2, n_samples))
    noise = noise_std * rng.standard_normal((1, n_samples))

    y = 3 * X[0:1, :] - 2 * X[1:2, :] + noise

    return X, y


def nonlinear_regression_data(
    n_samples=1000,
    noise_std=0.1,
    seed=42
):
    """
    Nonlinear dataset for testing representation power
    y = sin(x1) + 0.5 * x2^2 + noise
    """
    rng = np.random.default_rng(seed)

    X = rng.standard_normal((2, n_samples))
    noise = noise_std * rng.standard_normal((1, n_samples))

    y = np.sin(X[0:1, :]) + 0.5 * (X[1:2, :] ** 2) + noise

    return X, y