import numpy as np
import matplotlib.pyplot as plt

# Create a 10x10 array of purple pixels
pixels = np.array([[255, 0, 255] for _ in range(100)])

# Plot the array as an image
plt.imshow(pixels)
plt.show()