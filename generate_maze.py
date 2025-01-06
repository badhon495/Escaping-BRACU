from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import sys
from drawing_algorithms import midpoint_line, convert_coordinate, midpointcircle
from maze_points import get_maze_points


# Get the maze points
maze_points = get_maze_points()


# Window dimensions
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600


def plot_point(x, y):
    """Plot a single point using OpenGL."""
    glBegin(GL_POINTS)
    glVertex2f(x, y)
    glEnd()


def draw_maze():
    """Function to draw the maze structure."""
    global maze_points
    glColor3f(0, 0, 0)  # Set the color to black
    for i in range(len(maze_points)):
        midpoint_line(maze_points[i][0], maze_points[i][1], maze_points[i][2], maze_points[i][3])



def display():
    """Display callback for GLUT."""
    glClear(GL_COLOR_BUFFER_BIT)
    draw_maze()
    glFlush()

def reshape(width, height):
    """Handle window reshaping."""
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(-WINDOW_WIDTH // 2, WINDOW_WIDTH // 2, -WINDOW_HEIGHT // 2, WINDOW_HEIGHT // 2)
    glMatrixMode(GL_MODELVIEW)

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
    glutMainLoop()

if __name__ == "__main__":
    main()
