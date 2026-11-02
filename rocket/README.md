# rocket-ibr

`rocket-ibr` is a Python library that includes `Rocket`, `Shuttle`, and `CircleRocket` classes for simulation and object-oriented programming exercises.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install `rocket-ibr`:

```bash
pip install rocket-ibr
```

## Usage

```python
import rocket

# Create and move a Rocket
r = rocket.Rocket(x=0, y=0)
r.move_rocket(x_increment=1, y_increment=2)
print(r)

# Create a Shuttle
shuttle = rocket.Shuttle(x=5, y=10, flights_completed=3)
print(shuttle)

# Create a CircleRocket
cr = rocket.CircleRocket(x=2, y=5, radius=4)
print("Area:", cr.get_area())
print("Circumference:", cr.get_circumference())
```

## License
[MIT](https://choosealicense.com/licenses/mit/)