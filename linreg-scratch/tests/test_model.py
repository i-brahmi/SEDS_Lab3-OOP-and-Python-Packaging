import numpy as np
import pytest
from linreg_scratch import LinearRegression


def data():
    rng = np.random.default_rng(0)
    x = rng.uniform(0, 10, 100)
    y = 3 * x + 2 + rng.normal(0, 0.1, 100)
    return x, y


def test_closed_form():
    x, y = data()
    model = LinearRegression(solver="closed").fit(x, y)
    assert model.m == pytest.approx(3, abs=0.05)
    assert model.b == pytest.approx(2, abs=0.2)
    assert model.score(x, y) > 0.99


def test_gradient_descent():
    x, y = data()
    model = LinearRegression(lr=0.01, epochs=5000).fit(x, y)
    assert model.m == pytest.approx(3, abs=0.1)
    assert model.history[-1] < model.history[0]


def test_predict_before_fit():
    with pytest.raises(RuntimeError):
        LinearRegression().predict([1, 2])


def test_shape_mismatch():
    with pytest.raises(ValueError):
        LinearRegression().fit([1, 2, 3], [1, 2])
