import numpy as np
import matplotlib.pyplot as plt

# Define the phase function in polar coordinates
def phi1(r, theta):
    return np.sin(r**2 + theta)

# Convert Cartesian coordinates to polar coordinates
def cart2pol(x, y):
    r = np.sqrt(x**2 + y**2)
    theta = np.arctan2(y, x)
    return r, theta

# Create a grid of (x, y) values
x = np.linspace(-10, 10, 1000)
y = np.linspace(-10, 10, 1000)
X, Y = np.meshgrid(x, y)
R, Theta = cart2pol(X, Y)

# Compute the complex function T1
def T1(r, theta):
    return np.exp(1j * phi1(r, theta))

Z = T1(R, Theta)

# Compute the phase
phase = np.angle(Z)

# Plot the phase
plt.figure(figsize=(8, 8))
plt.imshow(phase, extent=(-10, 10, -10, 10), cmap='hsv', origin='lower')
plt.colorbar(label='Phase')
plt.title('Circular Moire Pattern from $T_1(r, \\theta) = \\exp[i\\Phi_1(r, \\theta)]$')
plt.xlabel('x')
plt.ylabel('y')
plt.show()
