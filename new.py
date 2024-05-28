import numpy as np
import matplotlib.pyplot as plt

# Constants
wavelength = 633e-9  # Wavelength of light in meters (example: 633nm)
theta = np.pi / 4  # Rotation angle between the two DOEs in radians

# Function to create an asymmetric Fresnel Zone Plate (FZP)
def create_asymmetric_fzp(radius, wavelength, focal_length, skew_factor):
    x = np.linspace(-radius, radius, 500)
    y = np.linspace(-radius, radius, 500)
    X, Y = np.meshgrid(x, y)
    R = np.sqrt((X + skew_factor)**2 + Y**2)
    phase = np.mod(2 * np.pi / wavelength * (R**2 / (2 * focal_length)), 2 * np.pi)
    return phase

# Create asymmetric DOE 1 and DOE 2
radius = 0.01  # 10 mm radius
focal_length1 = 0.1  # 100 mm focal length
focal_length2 = 0.15  # 150 mm focal length
skew_factor1 = 0.005  # Skew factor for DOE 1
skew_factor2 = -0.005  # Skew factor for DOE 2

doe1_phase = create_asymmetric_fzp(radius, wavelength, focal_length1, skew_factor1)
doe2_phase = create_asymmetric_fzp(radius, wavelength, focal_length2, skew_factor2)

# Rotate DOE 2
doe2_rotated_phase = np.mod(doe2_phase + theta, 2 * np.pi)

# Combine the phases to form the Moiré pattern
moire_phase = np.mod(doe1_phase + doe2_rotated_phase, 2 * np.pi)

# Calculate the focal length of the combined Moiré lens
def calculate_focal_length(wavelength, theta):
    return wavelength / (2 * np.pi * theta)

moire_focal_length = calculate_focal_length(wavelength, theta)

# Plotting the results
plt.figure(figsize=(12, 4))

plt.subplot(1, 3, 1)
plt.imshow(doe1_phase, cmap='gray')
plt.title('Asymmetric DOE 1 Phase')
plt.colorbar()

plt.subplot(1, 3, 2)
plt.imshow(doe2_rotated_phase, cmap='gray')
plt.title('Asymmetric DOE 2 Rotated Phase')
plt.colorbar()

plt.subplot(1, 3, 3)
plt.imshow(moire_phase, cmap='gray')
plt.title(f'Moiré Pattern\nFocal Length: {moire_focal_length:.2e} m')
plt.colorbar()

plt.tight_layout()
plt.show()
