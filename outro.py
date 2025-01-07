from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLUT.fonts import GLUT_BITMAP_HELVETICA_18, GLUT_BITMAP_TIMES_ROMAN_24
from drawing_algorithms import midpoint_line, convert_coordinate

# Window dimensions
W_WIDTH, W_HEIGHT = 1000, 800

# Global state variables to be imported from main.py
completed_level = 0
cumulative_gpa = 0.0

def draw_result_box(x, y, width, height, message):
    """Draw a result box with a specific message."""
    # Box outline
    glColor3f(0, 0.8, 1)  # Box border color
    midpoint_line(x - width/2, y - height/2, x + width/2, y - height/2)
    midpoint_line(x - width/2, y + height/2, x + width/2, y + height/2)
    midpoint_line(x - width/2, y - height/2, x - width/2, y + height/2)
    midpoint_line(x + width/2, y - height/2, x + width/2, y + height/2)
    
    # Text color
    glColor3f(1, 1, 1)
    
    # Calculate text position to center it in the box
    text_width = len(message) * 6  # Approximate character width
    text_x = x - text_width/2
    text_y = y
    
    glRasterPos2f(text_x, text_y)
    for ch in message:
        glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, ord(ch))

def display():
    """Render the outro screen with game results."""
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glClearColor(0, 0, 0, 0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    
    # Game Over Title
    glColor3f(1, 1, 1)
    glRasterPos2f(-100, 300)
    for ch in "GAME OVER":
        glutBitmapCharacter(GLUT_BITMAP_TIMES_ROMAN_24, ord(ch))
    
    # Display Total CGPA
    glColor3f(1, 1, 1)
    glRasterPos2f(-150, 250)
    cgpa_text = f"Total CGPA: {cumulative_gpa:.2f}"
    for ch in cgpa_text:
        glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, ord(ch))
    
    # Display Completed Level
    glColor3f(1, 1, 1)
    glRasterPos2f(-150, 220)
    level_text = f"Completed Level: {completed_level}"
    for ch in level_text:
        glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, ord(ch))
    
    # Determine result message based on level and CGPA
    if completed_level == 11:
        result_messages = [
            (4.0, "Wanna join as a faculty?"),
            (3.7, "Lost in jiboner mane, should have studied more in TARC"),
            (3.5, "Dont let the potential burn"),
            (3.0, "You have tried your best king"),
            (2.5, "Bro, start a business"),
            (2.0, "Touch some grass"),
            (0.0, "You are a disgrace")
        ]
        
        result_message = result_messages[-1][1]  # Default to lowest message
        for threshold, message in result_messages:
            if cumulative_gpa >= threshold:
                result_message = message
                break
    else:
        result_message = "You have potential to be a CEO"
    
    # Draw result box
    draw_result_box(0, 100, 400, 50, result_message)
    
    # Restart or Quit instructions
    glColor3f(1, 1, 1)
    glRasterPos2f(-150, -250)
    for ch in "Press R to Restart or Q to Quit":
        glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, ord(ch))
    
    glutSwapBuffers()

def keyboardListener(key, _, __):
    """Handle keyboard input for outro screen."""
    if key == b'r':
        # Restart the game
        print("Restarting Game...")
        # Add logic to reset game state
    elif key == b'q':
        # Quit the game
        print("Goodbye!")
        glutLeaveMainLoop()
        sys.exit(0)  # Ensure the program exits
    glutPostRedisplay()

def exit_game():
    """Exit the game and show the outro screen."""
    global completed_level, cumulative_gpa
    glutLeaveMainLoop()
    outro_main(completed_level, cumulative_gpa)

def init():
    """Initialize OpenGL settings."""
    glClearColor(0, 0, 0, 0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-250, 250, -400, 400, -1, 1)

def outro_main(level, cgpa):
    global completed_level, cumulative_gpa
    completed_level = level
    cumulative_gpa = cgpa
    glutInit()
    glutInitWindowSize(W_WIDTH, W_HEIGHT)
    glutInitWindowPosition(0, 0)
    glutInitDisplayMode(GLUT_DEPTH | GLUT_DOUBLE | GLUT_RGB)
    glutCreateWindow(b"Game Over")
    init()
    glutDisplayFunc(display)
    glutKeyboardFunc(keyboardListener)
    glutMainLoop()

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 3:
        print("Usage: python outro.py <completed_level> <cumulative_gpa>")
        sys.exit(1)
    completed_level = int(sys.argv[1])
    cumulative_gpa = float(sys.argv[2])
    outro_main(completed_level, cumulative_gpa)