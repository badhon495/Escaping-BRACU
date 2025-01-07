
from OpenGL.GLU import *
from random import randint as random
from OpenGL.GL import *
from OpenGL.GLUT import *
import random
import time
import math

# Window dimensions
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

# Player bubble properties
PLAYER_BUBBLE_RADIUS = 20
PLAYER_BUBBLE_X = WINDOW_WIDTH // 2
PLAYER_BUBBLE_Y = WINDOW_HEIGHT // 2
PLAYER_SPEED = 5

# Game state
CURRENT_LEVEL = 0
TOTAL_LEVELS = 11
SCORE = 0

# Border restriction types
BORDER_TYPES = [
    "zig-zag",
    "circular",
    "diagonal",
    "straight-curved",
    "breakable",
    "shifting",
    "random-shapes",
    "expanding-contracting",
    "rotating",
    "pulsing",
    "maze-like"
]

def init_opengl():
    glMatrixMode(GL_PROJECTION)
    gluPerspective(45, (WINDOW_WIDTH / WINDOW_HEIGHT), 0.1, 50.0)
    glMatrixMode(GL_MODELVIEW)
    glTranslatef(0.0, 0.0, -5)

def draw_player_bubble():
    glColor3f(1, 1, 1)
    glBegin(GL_POINTS)
    for angle in range(360):
        x = PLAYER_BUBBLE_X + PLAYER_BUBBLE_RADIUS * math.cos(math.radians(angle))
        y = PLAYER_BUBBLE_Y + PLAYER_BUBBLE_RADIUS * math.sin(math.radians(angle))
        glVertex2f(x, y)
    glEnd()

def draw_border_restrictions():
    glColor3f(1, 0, 0)
    border_type = BORDER_TYPES[CURRENT_LEVEL]

    if border_type == "zig-zag":
        # Draw zig-zag border
        pass
    elif border_type == "circular":
        # Draw circular border
        pass
    # Implement other border restriction types here
    else:
        # Draw default border
        glBegin(GL_LINE_LOOP)
        glVertex2f(50, 50)
        glVertex2f(WINDOW_WIDTH - 50, 50)
        glVertex2f(WINDOW_WIDTH - 50, WINDOW_HEIGHT - 50)
        glVertex2f(50, WINDOW_HEIGHT - 50)
        glEnd()

def update_player_position():
    global PLAYER_BUBBLE_X, PLAYER_BUBBLE_Y
    keys = glGetBooleanv(GL_CURRENT_BIT)
    if keys[ord('a')] or keys[ord('A')]:
        PLAYER_BUBBLE_X = max(PLAYER_BUBBLE_X - PLAYER_SPEED, PLAYER_BUBBLE_RADIUS)
    if keys[ord('d')] or keys[ord('D')]:
        PLAYER_BUBBLE_X = min(PLAYER_BUBBLE_X + PLAYER_SPEED, WINDOW_WIDTH - PLAYER_BUBBLE_RADIUS)
    if keys[ord('w')] or keys[ord('W')]:
        PLAYER_BUBBLE_Y = min(PLAYER_BUBBLE_Y + PLAYER_SPEED, WINDOW_HEIGHT - PLAYER_BUBBLE_RADIUS)
    if keys[ord('s')] or keys[ord('S')]:
        PLAYER_BUBBLE_Y = max(PLAYER_BUBBLE_Y - PLAYER_SPEED, PLAYER_BUBBLE_RADIUS)

def check_collision():
    global SCORE, CURRENT_LEVEL
    # Implement collision detection with border restrictions
    if CURRENT_LEVEL < TOTAL_LEVELS - 1 and SCORE >= (CURRENT_LEVEL + 1) * 100:
        CURRENT_LEVEL += 1
        SCORE = 0

def game_loop():
    global SCORE
    running = True
    while running:
        glClear(GL_COLOR_BUFFER_BIT)

        draw_player_bubble()
        draw_border_restrictions()
        update_player_position()
        check_collision()

        SCORE += 1
        glutSwapBuffers()

if __name__ == "__main__":
    glutInit()
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
    glutInitWindowSize(WINDOW_WIDTH, WINDOW_HEIGHT)
    glutCreateWindow("Bubble Restricted")
    init_opengl()
    glutDisplayFunc(game_loop)
    glutMainLoop()