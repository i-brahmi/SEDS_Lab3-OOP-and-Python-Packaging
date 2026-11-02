"""Simple linear regression (y = m*x + b) implemented from scratch with NumPy."""
import numpy as np


class LinearRegression:
    """Simple (one feature) linear regression.

    Parameters
    ----------
    lr : float
        Learning rate for gradient descent.
    epochs : int
        Number of gradient descent iterations.
    solver : {"gd", "closed"}
        "gd" uses gradient descent; "closed" uses the exact least-squares formula.

    Attributes
    ----------
    m : float
        Slope.
    b : float
        Intercept (bias).
    history : list of float
        MSE at each epoch (gradient descent only).
    """

    def __init__(self, lr=0.01, epochs=1000, solver="gd"):
        if solver not in ("gd", "closed"):
            raise ValueError("solver must be 'gd' or 'closed'")
        self.lr = lr
        self.epochs = epochs
        self.solver = solver
        self.m = 0.0
        self.b = 0.0
        self.history = []
        self._fitted = False

    @staticmethod
    def _to_1d(a, name):
        a = np.asarray(a, dtype=float).ravel()
        if a.size == 0:
            raise ValueError(f"{name} must not be empty")
        return a

    def fit(self, x, y):
        x = self._to_1d(x, "x")
        y = self._to_1d(y, "y")
        if x.shape != y.shape:
            raise ValueError("x and y must have the same length")
        n = len(x)

        if self.solver == "closed":
            x_mean, y_mean = x.mean(), y.mean()
            var = np.sum((x - x_mean) ** 2)
            if var == 0:
                raise ValueError("x has zero variance; cannot fit a line")
            self.m = float(np.sum((x - x_mean) * (y - y_mean)) / var)
            self.b = float(y_mean - self.m * x_mean)
        else:
            self.m, self.b = 0.0, 0.0
            self.history = []
            for _ in range(self.epochs):
                error = y - (self.m * x + self.b)
                d_m = (-2.0 / n) * np.sum(x * error)
                d_b = (-2.0 / n) * np.sum(error)
                self.m -= self.lr * d_m
                self.b -= self.lr * d_b
                self.history.append(float(np.mean(error ** 2)))

        self._fitted = True
        return self

    def predict(self, x):
        if not self._fitted:
            raise RuntimeError("Model is not fitted yet. Call fit() first.")
        return self.m * np.asarray(x, dtype=float) + self.b

    def mse(self, x, y):
        y = self._to_1d(y, "y")
        return float(np.mean((y - self.predict(self._to_1d(x, "x"))) ** 2))

    def score(self, x, y):
        """R^2 coefficient of determination."""
        y = self._to_1d(y, "y")
        pred = self.predict(self._to_1d(x, "x"))
        ss_res = np.sum((y - pred) ** 2)
        ss_tot = np.sum((y - y.mean()) ** 2)
        return float(1 - ss_res / ss_tot) if ss_tot != 0 else 0.0

    def __repr__(self):
        return f"LinearRegression(m={self.m:.4f}, b={self.b:.4f}, solver='{self.solver}')"
