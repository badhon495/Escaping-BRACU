maze_points_main =[
    [-340, 200, -220, 200],   # Horizontal line
    [-340, -200, -340, 200],  # Vertical line
    [-340, -200, 350, -200],  # Horizontal line
    [-220, 200, -220, -120],  # Vertical line
    [-20, -120, -200, -120],
    [-200, -120, -200, 100],
    [-200, 100, 170, 100], # the real vertical line [-340, 100, 350, 100]
    [170, 100, 170, 160],
    [170, 160, 350, 160],
    [350, 160, 350, -200],
    [240, -200, 240, 100],
]

def get_maze_points():
    return maze_points_main

