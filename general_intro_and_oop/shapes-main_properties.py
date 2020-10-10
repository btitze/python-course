"""Examples of how to use the shapes module."""

# Import the classes we use here (shapes_properties.py should be in the same directory):
from shapes_properties import Cube, Sphere


# The following creates a new object (my_cube) from the Cube class:
my_cube = Cube(position=(1, -2, 0.5), edge_length=5)
my_cube.draw()
print('My cube\'s volume: ', my_cube.volume())
print('My cube\'s surface: ', my_cube.surface(), '\n')

# The following creates a new object (my_sphere) from the Sphere class:
my_sphere = Sphere(position=(12.2, 0, -17.87), radius=7.5)
my_sphere.draw()

# Now there is error handling when we try to set a negativ radius:
# Try: my_sphere.radius = -7.5
my_sphere.radius = 7.5

# Volume and surface can be accessed as attributes now:
print('My sphere\'s volume: ', my_sphere.volume)
print('My sphere\'s surface: ', my_sphere.surface, '\n')

# What is the distance between my_square and my_cube?
print('The distance between my cube and my sphere is: ',
      my_cube.distance_to(my_sphere), '\n')

# We can now create a unit sphere with the new class method:
my_unit_sphere = Sphere.unit_sphere()
print('My unit sphere\'s radius: ', my_unit_sphere.radius)
