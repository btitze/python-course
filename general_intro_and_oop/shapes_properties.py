"""A simple module for 3D shapes to learn basic OOP concepts. This version uses properties for the Sphere class."""

import math

class Shape3D:
    """The base class for 3D shapes."""

    def __init__(self, position):
        # Every 3D shape has a position in space:
        self.position = position   # tuple of coordinates: (x, y, z)

    def draw(self):
        raise NotImplementedError('Error: An abstract shape cannot be drawn.')

    def distance_to(self, other_shape):
        """Calculate the distance between two objects."""
        x0, y0, z0 = self.position
        x1, y1, z1 = other_shape.position
        euclidean_distance = math.sqrt(
            (x0 - x1)**2 + (y0 - y1)**2 + (z0 - z1)**2)
        return euclidean_distance


class Cube(Shape3D):
    """The class for cubes, inherits from the base class Shape3D."""

    def __init__(self, position, edge_length):
        # First, call the parent:
        super().__init__(position)
        self.edge_length = edge_length
        print('A cube was created!')

    def volume(self):
        return self.edge_length**3

    def surface(self):
        return 6 * self.edge_length**2

    def draw(self):
        print(f'A cube with an edge length of {self.edge_length} is being '
              f'drawn at position {self.position}.')


class Sphere(Shape3D):
    """The class for spheres, inherits from the base class Shape3D.
    Here we use properties.
    """

    def __init__(self, position, radius):
        # First, call the parent:
        super().__init__(position)
        self.radius = radius
        print('A sphere was created!')

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, radius):
        if radius >= 0:
            self._radius = radius
        else:
            raise ValueError('Radius cannot be negative!')

    # volume and surface can be accessed as attributes:
    @property
    def volume(self):
        return 4/3 * math.pi * self.radius**3

    @property
    def surface(self):
        return 4 * math.pi * self.radius**2

    def draw(self):
        print(f'A sphere with a radius of {self.radius} is being '
              f'drawn at position {self.position}.')

    # This class method is not bound to an object (self) but to the class (cls).
    # It's a 'factory method' that creates a default instance of the class (a unit sphere in our case.)
    @classmethod
    def unit_sphere(cls):
        """Return unit sphere at the origin."""
        return cls((0, 0, 0), 1.0)