from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import sys
from drawing_algorithms import midpoint_line, convert_coordinate, midpointcircle


# Window dimensions
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600


def plot_point(x, y):
    """Plot a single point using OpenGL."""
    glBegin(GL_POINTS)
    glVertex2f(x, y)
    glEnd()

# Import your midpoint_line, midpointcircle, and other functions here
# Example: from algorithms import midpoint_line, midpointcircle

def draw_maze():
    """Function to draw the maze structure."""
    glColor3f(0, 0, 0)  # Set the color to black
    
    # Example maze structure
    midpoint_line(-350, -250, -350, 250)  # Vertical line
    midpoint_line(-350, 250, 350, 250)    # Horizontal line
    midpoint_line(350, 250, 350, -250)    # Vertical line
    midpoint_line(350, -250, -350, -250)  # Horizontal line

    # draw the maze using midpoint_line
    midpoint_line(-300, -200, -150, -200) #horizontal line
    midpoint_line(-300, 200, -150, 200) #horizontal line
    midpoint_line(-300, -200, -300, 200) #vertical line
    midpoint_line(-150, -100, -150, 200) #vertical line

    #draw a horizontal line from -150, -100
    midpoint_line(-150, -100, 100, -100)
    #draw a horizontal line from -300, -200
    midpoint_line(-150, -200, 300, -200)
    #draw a vertical line from 300, -200
    midpoint_line(300, -200, 300, 200)
    #draw a horizontal line from 100, -100
    midpoint_line(100, -100, 100, 200)
    midpoint_line(100, 200, 300, 200)


   



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
