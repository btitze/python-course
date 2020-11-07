# This is a quick check if the required libraries are installed and working.
# Copy and paste the following code into a Jupyter Notebook and run it there.

from PIL import Image, ImageFilter
from skimage import data, filters
from scipy import misc, ndimage
import numpy as np

from IPython.display import display
import matplotlib.pyplot as plt
%matplotlib inline

try:
    my_image = Image.open('img\\monarch_testimage.png')
except:
    print('Error: Could not load test image!')
else:
    # PIL and NumPy
    print(f'Loaded image (PIL):\n'
          f'Format: {my_image.format}\n'
          f'Size: {my_image.size}\n'
          f'Mode: {my_image.mode}')
    my_image_np = np.asarray(my_image)
    print(f'Image as NumPy array:\n'
          f'Shape: {my_image_np.shape}\n'
          f'Mean: {my_image_np.mean()}\n'
          f'StdDev: {my_image_np.std()}\n')
    display(my_image.filter(ImageFilter.FIND_EDGES))
    # scikit-image
    moon_image = data.moon()
    fig, ax = filters.try_all_threshold(moon_image, figsize=(12, 10), verbose=False)
    plt.show()
    # SciPy
    racoon_face = misc.face()
    blurred_racoon_face = ndimage.gaussian_filter(racoon_face, sigma=6)
    plt.imshow(blurred_racoon_face)