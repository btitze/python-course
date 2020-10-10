"""A simple module for 3D shapes to learn basic OOP concepts."""

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
    """The class for spheres, inherits from the base class Shape3D."""

    def __init__(self, position, radius):
        # First, call the parent:
        super().__init__(position)
        self.radius = radius
        print('A sphere was created!')

    def volume(self):
        return 4/3 * math.pi * self.radius**3

    def surface(self):
        return 4 * math.pi * self.radius**2

    def draw(self):
        print(f'A sphere with a radius of {self.radius} is being '
              f'drawn at position {self.position}.')
