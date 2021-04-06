import numpy as np
from PIL import Image
# Create a NumPy array, which has four elements. The top-left should be pure red, the top-right should be pure blue, the bottom-left should be pure green, and the bottom-right should be yellow
pixels = np.array([[[255, 0, 0], [0, 255, 0]], [[0, 0, 255], [255, 255, 0]]])

image = Image.fromarray(pixels.astype('uint8'), 'RGB')


# Save the image
image.save('image.png')