# rocket.py
from math import pi, sqrt


class Rocket:
    """Rocket simulates a rocket ship for a game or a physics simulation."""

    def __init__(self, x=0, y=0):
        # Each rocket has an (x, y) position.
        self.x = x
        self.y = y

    def move_rocket(self, x_increment=0, y_increment=1):
        """Move the rocket according to the parameters given.

        Default behavior is to move the rocket up one unit.
        """
        self.x += x_increment
        self.y += y_increment

    def get_distance(self, other_rocket):
        """Calculates the distance from this rocket to another rocket."""
        distance = sqrt(
            (self.x - other_rocket.x) ** 2 + (self.y - other_rocket.y) ** 2
        )
        return distance

    def __eq__(self, other):
        """Two rockets are equal if they share the exact same (x, y) position."""
        if not isinstance(other, Rocket):
            return False
        return self.x == other.x and self.y == other.y

    def __str__(self):
        return f"A Rocket positioned at ({self.x},{self.y})"

    def __repr__(self):
        return f"Rocket({self.x},{self.y})"


class Shuttle(Rocket):
    """Shuttle simulates a space shuttle, which is really just a reusable rocket."""

    def __init__(self, x=0, y=0, flights_completed=0):
        super().__init__(x, y)
        self.flights_completed = flights_completed

    def __str__(self):
        return f"A Shuttle positioned at ({self.x},{self.y}) with {self.flights_completed} flights completed"

    def __repr__(self):
        return f"Shuttle(x={self.x}, y={self.y}, flights_completed={self.flights_completed})"


class CircleRocket(Rocket):
    """CircleRocket simulates a circular rocket ship with a specific radius."""

    def __init__(self, x=0, y=0, radius=1):
        super().__init__(x, y)
        self.radius = radius

    def get_area(self):
        """Calculates and returns the cross-sectional area of the circular rocket."""
        return pi * (self.radius**2)

    def get_circumference(self):
        """Calculates and returns the circumference of the circular rocket."""
        return 2 * pi * self.radius

    def __str__(self):
        return f"A CircleRocket positioned at ({self.x},{self.y}) with radius {self.radius}"

    def __repr__(self):
        return f"CircleRocket(x={self.x}, y={self.y}, radius={self.radius})"