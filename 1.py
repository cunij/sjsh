import numpy as np
import matplotlib.pyplot as plt

# Define the phase function in polar coordinates
def phi1(r, theta):
    return r**2 + theta

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

# Compute the phase
phase = phi1(R, Theta)

# Plot the phase
plt.figure(figsize=(8, 8))
plt.imshow(phase, extent=(-10, 10, -10, 10), cmap='hsv', origin='lower')
plt.colorbar(label='Phase')
plt.title('Phase Function $\Phi_1(r, \\theta) = r^2 + \\theta$')
plt.xlabel('x')
plt.ylabel('y')
plt.show()
def T1(r, theta):
    return np.exp(1j * phi1(r, theta))

Z = T1(R, Theta)
phase_pattern = np.angle(Z)

# Plot the phase pattern
plt.figure(figsize=(8, 8))
plt.imshow(phase_pattern, extent=(-10, 10, -10, 10), cmap='hsv', origin='lower')
plt.colorbar(label='Phase')
plt.title('Moire Pattern from $T_1(r, \\theta) = \\exp[i\\Phi_1(r, \\theta)]$')
plt.xlabel('x')
plt.ylabel('y')
plt.show()

# Perform Fourier Transform
F = np.fft.fftshift(np.fft.fft2(phase_pattern))
F_magnitude = np.abs(F)
F_phase = np.angle(F)

# Plot the magnitude of the Fourier transform
plt.figure(figsize=(8, 8))
plt.imshow(np.log(F_magnitude), extent=(-10, 10, -10, 10), cmap='viridis', origin='lower')
plt.colorbar(label='Log Magnitude')
plt.title('Fourier Transform Magnitude of the Moire Pattern')
plt.xlabel('kx')
plt.ylabel('ky')
plt.show()
