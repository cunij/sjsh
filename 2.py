import numpy as np
import matplotlib.pyplot as plt

def generate_moire_pattern(size, num_rings, ring_width):
    """
    Generate a Moire pattern with concentric rings.

    Parameters:
        - size: Size of the image (height, width).
        - num_rings: Number of concentric rings.
        - ring_width: Width of each ring.

    Returns:
        - moire_pattern: Generated Moire pattern image.
    """
    # Create a grid of coordinates
    x = np.linspace(-1, 1, size[1])
    y = np.linspace(-1, 1, size[0])
    X, Y = np.meshgrid(x, y)

    # Calculate the distance from the center
    radius = np.sqrt(X**2 + Y**2)

    # Generate Moire pattern with concentric rings
    moire_pattern = np.zeros(size)
    for i in range(1, num_rings + 1):
        ring = np.logical_and(radius >= (i - 0.5) * ring_width, radius <= (i + 0.5) * ring_width)
        moire_pattern += ring

    return moire_pattern

# Define the size and parameters of the Moire pattern
image_size = (400, 400)  # Image size (height, width)
num_rings = 10  # Number of concentric rings
ring_width = 0.05  # Width of each ring

# Generate the Moire pattern with concentric rings
moire_pattern = generate_moire_pattern(image_size, num_rings, ring_width)

# Plot the Moire pattern
plt.imshow(moire_pattern, cmap='gray')
plt.title('Moire Pattern with Concentric Rings')
plt.axis('off')
plt.show()
