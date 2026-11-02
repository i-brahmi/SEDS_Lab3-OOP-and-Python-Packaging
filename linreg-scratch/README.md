# linreg-scratch

Simple linear regression (`y = m*x + b`) implemented from scratch with NumPy.

## Install

```bash
pip install linreg-scratch
```

## Usage

```python
import numpy as np
from linreg_scratch import LinearRegression

x = np.array([1, 2, 3, 4, 5])
y = np.array([3, 5, 7, 9, 11])

model = LinearRegression(lr=0.01, epochs=5000)   # gradient descent
model.fit(x, y)

print(model.m, model.b)       # slope, intercept
print(model.predict([6, 7]))  # predictions
print(model.score(x, y))      # R^2

# exact solution instead of gradient descent
LinearRegression(solver="closed").fit(x, y)
```

## Development

```bash
pip install -e . pytest
pytest
```
