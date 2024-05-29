import matplotlib.pyplot as plt
import numpy as np

def hexagon(x_center, y_center, size):
    """Generate the vertices of a hexagon centered at (x_center, y_center) with a given size."""
    angles = np.linspace(0, 2 * np.pi, 7)
    x_hex = x_center + size * np.cos(angles)
    y_hex = y_center + size * np.sin(angles)
    return x_hex, y_hex

def draw_hex_tiling(center_x=0, center_y=0, interval=10, size=5, angles=[0, 90], colors=['red', 'blue'], linewidth=0.5):
    # Initialize the graph
    fig, ax = plt.subplots(figsize=(10, 10))
    
    # Draw hexagon tiles for each angle
    for idx, angle in enumerate(angles):
        # Convert angle to radians
        angle_rad = np.deg2rad(angle)
        
        # Rotation transformation matrix
        cos_angle = np.cos(angle_rad)
        sin_angle = np.sin(angle_rad)
        
        # Calculate the height of the hexagon
        hex_height = np.sqrt(3) * size
        
        # Set wider range to fill the screen
        for i in range(-50, 51):
            for j in range(-50, 51):
                # Calculate the coordinates of the honeycomb structure
                x = i * 1.5 * size
                y = j * hex_height + (i % 2) * hex_height / 2
                
                # Calculate the relative position from the center
                x_rel = x - center_x
                y_rel = y - center_y
                
                # Apply rotation
                x_rot = x_rel * cos_angle - y_rel * sin_angle
                y_rot = x_rel * sin_angle + y_rel * cos_angle
                
                # Restore the rotated coordinates to the center
                x_final = x_rot + center_x
                y_final = y_rot + center_y
                
                # Generate and plot the hexagon
                x_hex, y_hex = hexagon(x_final, y_final, size)
                ax.plot(x_hex, y_hex, color=colors[idx % len(colors)], linewidth=linewidth)
    
    # Set axes limits
    ax.set_xlim(-100, 100)
    ax.set_ylim(-100, 100)
    ax.set_aspect('equal')
    
    plt.grid(False)
    plt.show()

# Example: Draw honeycomb hexagons with angles 0 and 3 degrees, colors red and blue, line width 1.0
draw_hex_tiling(center_x=0, center_y=0, interval=2, size=2, angles=[0, 3], colors=['red', 'blue'], linewidth=1.0)
