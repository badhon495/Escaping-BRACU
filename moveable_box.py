from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from drawing_algorithms import midpoint_line

# Initial box position
box_x = 0
box_y = 0
box_size = 15  # 15-pixel square

# Function to draw the box
def draw_box(x, y, size):
    """Draw a square box using midpoint_line."""
    half_size = size // 2
    midpoint_line(x - half_size, y - half_size, x + half_size, y - half_size)  # Bottom
    midpoint_line(x + half_size, y - half_size, x + half_size, y + half_size)  # Right
    midpoint_line(x + half_size, y + half_size, x - half_size, y + half_size)  # Top
    midpoint_line(x - half_size, y + half_size, x - half_size, y - half_size)  # Left

# Function to display the scene
def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1, 0, 0)  # Set box color (red)
    draw_box(box_x, box_y, box_size)  # Draw the box
    glFlush()

# Function to handle arrow key presses
def special_keys(key, x, y):
    global box_x, box_y
    move_step = 10 

    if key == GLUT_KEY_UP:       # Move up
        box_y += move_step
    elif key == GLUT_KEY_DOWN:   # Move down
        box_y -= move_step
    elif key == GLUT_KEY_LEFT:   # Move left
        box_x -= move_step
    elif key == GLUT_KEY_RIGHT:  # Move right
        box_x += move_step



    # Redisplay the scene with the updated box position
    glutPostRedisplay()

# Function to initialize the OpenGL environment
def init():
    glClearColor(1, 1, 1, 1)  # Set background color to white
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(-400, 400, -300, 300)  # Set coordinate system for 800x600 screen

# Main function
def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(800, 600)
    glutCreateWindow(b"Movable Box")  # Use byte string for the title
    init()
    glutDisplayFunc(display)
    glutSpecialFunc(special_keys)  # Register arrow key event handler
    glutMainLoop()


if __name__ == "__main__":
    main()
