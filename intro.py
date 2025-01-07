from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLUT.fonts import GLUT_BITMAP_HELVETICA_18, GLUT_BITMAP_TIMES_ROMAN_24
from drawing_algorithms import midpoint_line, convert_coordinate, midpointcircle

# Window dimensions
W_WIDTH, W_HEIGHT = 1000, 800

# Global state variables
game_state = 'intro'

def draw_button(x, y, width, height, label):
    """Draw a button with label."""
    glColor3f(0, 0.8, 1)  # Button color
    
    # Button outline
    midpoint_line(x - width/2, y - height/2, x + width/2, y - height/2)
    midpoint_line(x - width/2, y + height/2, x + width/2, y + height/2)
    midpoint_line(x - width/2, y - height/2, x - width/2, y + height/2)
    midpoint_line(x + width/2, y - height/2, x + width/2, y + height/2)
    
    # Add label to the button
    glColor3f(1, 1, 1)
    glRasterPos2f(x - 30, y - 5)
    for ch in label:
        glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, ord(ch))

def display():
    """Render the intro screen."""
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glClearColor(0, 0, 0, 0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    
    # Game Title
    glColor3f(1, 1, 1)
    glRasterPos2f(-50, 200)
    for ch in "Escaping BRACU":
        glutBitmapCharacter(GLUT_BITMAP_TIMES_ROMAN_24, ord(ch))
    
    # Game Subtitle
    glRasterPos2f(-100, 180)
    for ch in "A game of tension, depression and hair loss":
        glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, ord(ch))
    
    # Play Button
    draw_button(0, 0, 100, 50, "Press P to Play")
    
    # Quit Button
    draw_button(0, -100, 100, 50, "Quit (Q)")
    
    glutSwapBuffers()

def keyboardListener(key, _, __):
    """Handle keyboard input for intro screen."""
    global game_state
    if key == b'p':
        # Transition to game
        print("Starting Game...")
        game_state = 'game'
        start_game()
    elif key == b'q':
        # Quit the game
        print("Goodbye!")
        glutLeaveMainLoop()
    glutPostRedisplay()

def mouseListener(button, state, x, y):
    """Handle mouse input for intro screen."""
    if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
        c_x, c_y = convert_coordinate(x, y, W_WIDTH, W_HEIGHT)
        
        # Play button area
        if -50 < c_x < 50 and -25 < c_y < 25:
            print("Starting Game...")
            game_state = 'game'
            start_game()
        
        # Quit button area
        elif -50 < c_x < 50 and -125 < c_y < -75:
            print("Goodbye!")
            glutLeaveMainLoop()
    glutPostRedisplay()

def init():
    """Initialize OpenGL settings."""
    glClearColor(0, 0, 0, 0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-250, 250, -400, 400, -1, 1)

def intro_main(start_game_func):
    global start_game
    start_game = start_game_func
    glutInit()
    glutInitWindowSize(W_WIDTH, W_HEIGHT)
    glutInitWindowPosition(0, 0)
    glutInitDisplayMode(GLUT_DEPTH | GLUT_DOUBLE | GLUT_RGB)
    glutCreateWindow(b"Escaping BRACU")
    init()
    glutDisplayFunc(display)
    glutKeyboardFunc(keyboardListener)
    glutMouseFunc(mouseListener)
    glutMainLoop()