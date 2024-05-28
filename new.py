import numpy as np
import matplotlib.pyplot as plt

# Constants
wavelength = 633e-9  # Wavelength of light in meters (example: 633 nm)
f1 = 0.1  # Focal length of DOE 1 (100 mm)
f2 = 0.15  # Focal length of DOE 2 (150 mm)
theta = np.pi / 4  # Rotation angle for DOE 2 (45 degrees)

# Grid
x = np.linspace(-0.01, 0.01, 500)
y = np.linspace(-0.01, 0.01, 500)
X, Y = np.meshgrid(x, y)
R = np.sqrt(X**2 + Y**2)
Phi = np.arctan2(Y, X)

# Asymmetric Phase profiles
Phi1 = (np.pi * (X**2 + 2*Y**2)) / (wavelength * f1)
Phi2 = (np.pi * (2*X**2 + Y**2)) / (wavelength * f2) + theta * Phi

# Adjust Phi1 to create the asymmetric profile similar to the provided image
Phi1_asymmetric = (np.pi * (X**2 + 2*(Y - 0.005)**2)) / (wavelength * f1)

# Rotate DOE 2
def rotate_phase(Phi, angle):
    cos_angle = np.cos(angle)
    sin_angle = np.sin(angle)
    X_rot = cos_angle * X + sin_angle * Y
    Y_rot = -sin_angle * X + cos_angle * Y
    R_rot = np.sqrt(X_rot**2 + Y_rot**2)
    return np.mod((np.pi * (2*X_rot**2 + Y_rot**2)) / (wavelength * f2), 2 * np.pi)

Phi2_rotated = rotate_phase(Phi2, theta)

# Combined phase profile
Phi_combined = np.mod(Phi1_asymmetric + Phi2_rotated, 2 * np.pi)

# Plotting
plt.figure(figsize=(18, 6))

plt.subplot(1, 3, 1)
plt.imshow(Phi1_asymmetric, extent=(-0.01, 0.01, -0.01, 0.01), cmap='gray')
plt.title('DOE 1 Asymmetric Phase Profile')
plt.colorbar()

plt.subplot(1, 3, 2)
plt.imshow(Phi2_rotated, extent=(-0.01, 0.01, -0.01, 0.01), cmap='gray')
plt.title('DOE 2 Rotated Phase Profile')
plt.colorbar()

plt.subplot(1, 3, 3)
plt.imshow(Phi_combined, extent=(-0.01, 0.01, -0.01, 0.01), cmap='gray')
plt.title('Combined Phase Profile')
plt.colorbar()

plt.tight_layout()
plt.show()
