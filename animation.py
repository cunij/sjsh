import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import matplotlib.animation as animation

# Load and process the silhouette image
def load_silhouette(image_path):
    image = Image.open(image_path).convert('L')  # Convert to grayscale
    image = image.point(lambda x: 0 if x < 128 else 255, '1')  # Binarize
    return np.array(image)

# Draw vertical white lines
def draw_fixed_white_lines(ax, interval=10):
    positions = np.arange(-200, 200, interval)
    for pos in positions:
        x_start = pos
        x_end = pos
        y_start = -100
        y_end = 100
        ax.plot([x_start, x_end], [y_start, y_end], color='w', linewidth=5)

# Draw moving black lines
def draw_moving_black_lines(ax, offset, interval=10):
    positions = np.arange(-200, 200, interval)
    for pos in positions:
        x_start = pos + offset
        x_end = pos + offset
        y_start = -100
        y_end = 100
        ax.plot([x_start, x_end], [y_start, y_end], color='k', linewidth=5)

# Apply and animate vertical lines effect
def animate_vertical_lines(silhouette, interval=10, speed=0.1):
    fig, ax = plt.subplots(figsize=(10, 10))
    
    # Draw the silhouette and fixed white lines initially
    ax.imshow(silhouette, cmap='gray', extent=[-100, 100, -100, 100])
    draw_fixed_white_lines(ax, interval)
    
    def update(frame):
        ax.clear()
        ax.imshow(silhouette, cmap='gray', extent=[-100, 100, -100, 100])
        draw_fixed_white_lines(ax, interval)
        draw_moving_black_lines(ax, frame, interval)
        ax.set_xlim(-100, 100)
        ax.set_ylim(-100, 100)
        ax.axis('off')

    ani = animation.FuncAnimation(fig, update, frames=np.arange(-200, 200, speed), interval=10, repeat=True)
    plt.show()

# Load the silhouette image
silhouette = load_silhouette('image.png')

# Animate the vertical lines effect
animate_vertical_lines(silhouette, interval=10, speed=0.1)
