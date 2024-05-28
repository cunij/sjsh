import numpy as np
import matplotlib.pyplot as plt

# Define the grid
x = np.linspace(0, 10, 500)
y = np.linspace(0, 10, 500)
X, Y = np.meshgrid(x, y)

# Define the spatial frequencies for the patterns
k_r = 10  # spatial frequency of reference pattern
k_d = 10  # spatial frequency of deformed pattern (could be the same or slightly different)

# Generate the reference pattern (I_r)
I_r = np.cos(k_r * X)

# Define a surface with height variations (h)
h = np.sin(2 * np.pi * X / 5) * np.sin(2 * np.pi * Y / 5)

# Generate the deformed pattern (I_d) with height variations
lambda_pattern = 1  # wavelength of the pattern
phi_d = 2 * np.pi * h / lambda_pattern
I_d = np.cos(k_d * X + phi_d)

# Generate the Moire pattern (I_m)
I_m = I_r * I_d

# Plot the patterns
fig, axs = plt.subplots(1, 3, figsize=(15, 5))
axs[0].imshow(I_r, cmap='gray')
axs[0].set_title('Reference Pattern (I_r)')
axs[0].axis('off')

axs[1].imshow(I_d, cmap='gray')
axs[1].set_title('Deformed Pattern (I_d)')
axs[1].axis('off')

axs[2].imshow(I_m, cmap='gray')
axs[2].set_title('Moire Pattern (I_m)')
axs[2].axis('off')

plt.show()
