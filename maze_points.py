
maze_points_1 = [
    [-300, -200, -150, -200], # Horizontal line
    [-300, 200, -150, 200],   # Horizontal line
    [-300, -200, -300, 200],  # Vertical line
    [-150, -100, -150, 200],  # Vertical line

    [-150, -100, 100, -100],  # Horizontal line
    [-150, -200, 300, -200],  # Horizontal line
    [300, -200, 300, 200],    # Vertical line
    [100, -100, 100, 200],    # Vertical line
    [100, 200, 300, 200]      # Horizontal line
]

# Define the maze points array
maze_points_2 = [
    # Outer rectangle
    [-350, -250, -350, 250],  # Vertical line (left)
    [-350, 250, 350, 250],    # Horizontal line (top)
    [350, 250, 350, -250],    # Vertical line (right)
    [350, -250, -350, -250],  # Horizontal line (bottom)

    # Inner structure
    [-300, -200, 300, -200],  # Bottom horizontal line
    [-300, 200, -300, -200],  # Left vertical line
    [300, -200, 300, 200],    # Right vertical line

    # Upper horizontal segments
    [-300, 200, -180, 200],   # Left top segment
    [-180, 0, -60, 0],        # Middle bottom segment
    [-60, 200, 60, 200],      # Middle top segment
    [60, 0, 180, 0],          # Middle bottom segment
    [180, 200, 300, 200],     # Right top segment

    # Vertical dividers
    [-180, 200, -180, 0],     # Left vertical segment
    [-60, 200, -60, 0],       # Middle-left vertical segment
    [60, 200, 60, 0],         # Middle-right vertical segment
    [180, 200, 180, 0]        # Right vertical segment
]


def get_maze_points():
    return maze_points_2

