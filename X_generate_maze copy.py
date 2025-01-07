from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import sys
from drawing_algorithms import midpoint_line, convert_coordinate, midpointcircle
from CG_calc import calculate_cg

# Window dimensions
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

# Maze points for level 2
maze_points_2 = [
    # Outer rectangle
    [-350, -250, -350, 250],  # Vertical line (left)
    [-350, 250, 350, 250],    # Horizontal line (top)
    [350, 250, 350, -250],    # Vertical line (right)
    [350, -250, -350, -250],  # Horizontal line (bottom)

    # Inner structure
    [-300, -200, 260, -200],  # Bottom horizontal line 
    [-300, 200, -300, -200],  # Left vertical line
    [300, -200, 300, 200],    # Right vertical line

    # Upper horizontal segments
    [-300, 200, -230, 200],   # Left top segment
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

# Ball position
ball_x, ball_y = -340, -240
ball_radius = 10
current_cg = 4.0
semester = 1
total_cg = current_cg

def plot_point(x, y):
    """Plot a single point using OpenGL."""
    glBegin(GL_POINTS)
    glVertex2f(x, y)
    glEnd()

def draw_maze(maze_points):
    """Function to draw the maze structure."""
    glColor3f(0, 0, 0)  # Set the color to black
    for i in range(len(maze_points)):
        midpoint_line(maze_points[i][0], maze_points[i][1], maze_points[i][2], maze_points[i][3])

def draw_ball(x, y, radius, cg):
    """Function to draw the ball."""
    glColor3f(1, 0, 0)  # Set the color to red
    midpointcircle(radius, x, y)
    glColor3f(0, 0, 0)  # Set the color to black
    glRasterPos2f(x - 5, y - 5)
    for char in f"{cg:.2f}":
        glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, ord(char))

def draw_cgpa_box(cgpa):
    """Function to draw the CGPA box."""
    glColor3f(0, 0, 0)  # Set the color to black
    midpoint_line(200, 200, 300, 200)
    midpoint_line(200, 200, 200, 250)
    midpoint_line(300, 200, 300, 250)
    midpoint_line(200, 250, 300, 250)
    glRasterPos2f(210, 220)
    for char in f"CGPA: {cgpa:.2f}":
        glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, ord(char))

def display():
    """Display callback for GLUT."""
    glClear(GL_COLOR_BUFFER_BIT)
    draw_maze(maze_points_2)
    draw_ball(ball_x, ball_y, ball_radius, current_cg)
    draw_cgpa_box(total_cg)
    glFlush()

def reshape(width, height):
    """Handle window reshaping."""
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(-WINDOW_WIDTH // 2, WINDOW_WIDTH // 2, -WINDOW_HEIGHT // 2, WINDOW_HEIGHT // 2)
    glMatrixMode(GL_MODELVIEW)

def keyboard_listener(key, _, __):
    """Handle keyboard input."""
    global ball_x, ball_y, current_cg, semester, total_cg
    if key == b'w' and ball_y + ball_radius < 250:
        ball_y += 10
    elif key == b's' and ball_y - ball_radius > -250:
        ball_y -= 10
    elif key == b'a' and ball_x - ball_radius > -350:
        ball_x -= 10
    elif key == b'd' and ball_x + ball_radius < 350:
        ball_x += 10
    current_cg = calculate_cg(current_cg, semester, total_cg)
    glutPostRedisplay()

def main():
    """Main function to set up OpenGL with GLUT."""
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(WINDOW_WIDTH, WINDOW_HEIGHT)
    glutCreateWindow(b"Midpoint Maze Drawing")
    glClearColor(1.0, 1.0, 1.0, 1.0)  # Set background color to white
    glColor3f(0.0, 0.0, 0.0)          # Set drawing color to black
    glPointSize(2)                    # Set point size
    glutDisplayFunc(display)
    glutReshapeFunc(reshape)
    glutKeyboardFunc(keyboard_listener)
    glutMainLoop()

if __name__ == "__main__":
    main()
