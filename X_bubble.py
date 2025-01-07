from OpenGL.GLU import *
from random import randint as random
from OpenGL.GL import *
from OpenGL.GLUT import *
import random
import time
import math
from drawing_algorithms import midpointcircle, midpoint_line


# WINDOW_WIDTH = 800
# WINDOW_HEIGHT = 600

W_WIDTH, W_HEIGHT = 800, 600 # Window dimensions
fliper = 1
# W_WIDTH, W_HEIGHT = 500, 800 # Window dimensions
bullet_list = [] 
bubble_list = [] 
score = 0 
misfires = 0 
freeze = False 
gameover = 0  
last_frame_time = 0 
bullet_speed = 300 
rocket_x = 0 


############################################################################################################
def create_bubble(existing_bubbles):
    """
    Generate a random position for a bubble within the specified range.
    Horizontal range: -200 to 170
    Vertical range: -200 to 100
    """
    global score
    is_dynamic = False
    if score > 10:
        is_dynamic = random.random() < 0.30 
    r = random.randint(10, 20) 
    color = [0, 0, 0] 
    while True:
        x = random.randint(-200, 170)  # Random x-coordinate within horizontal range
        y = random.randint(-200, 100)  # Random y-coordinate within vertical range

        if not check_bubble_overlap(x, y, r, existing_bubbles):
            bubble = {
                'x': x, 
                'y': y, 
                'r': 7, 
                'color': color,
                'is_dynamic': is_dynamic,
                'dynamic_phase': 0, 
                'dynamic_direction': 1 
            }
            return bubble
############################################################################################################
def check_bubble_overlap(x, y, r, other_bubbles):
    for other in other_bubbles:
        distance = ((x - other['x']) ** 2 + (y - other['y']) ** 2) ** 0.5
        if other['is_dynamic'] and distance < (r + 25):
            return True
        elif not other['is_dynamic'] and distance < (r + other['r']):
            return True
    return False
############################################################################################################

def plot_point(x, y):
    glBegin(GL_POINTS)
    glVertex2f(x, y)
    glEnd()

#Returns the x position of a bubble.
def bubble_x_position(bubble):
    return bubble['x']
############################################################################################################
def draw_bullet():
    global bullet_list
    glColor3f(1, 1, 1)
    for bullet in bullet_list:
        midpointcircle(8, bullet[0], bullet[1]) 
############################################################################################################
def draw_bubble():
    global bubble_list
    for bubble in bubble_list:
        glColor3f(bubble['color'][0], bubble['color'][1], bubble['color'][2])
        midpointcircle(bubble['r'], bubble['x'], bubble['y'])
############################################################################################################
def draw_ui():
    global rocket_x, score, misfires, freeze
    glPointSize(2)
    glColor3f(1, 1, 1)

############################################################################################################
def convert_coordinate(x, y):
    a = x - (W_WIDTH / 2)
    b = (W_HEIGHT / 2) - y
    return a, b
############################################################################################################
def animate():
    global freeze, bubble_list, gameover, score, bullet_list, misfires, last_frame_time, rocket_x
    current_time = time.time()
    delta_time = current_time - last_frame_time
    last_frame_time = current_time
    global fliper

    if not freeze and gameover < 3 and misfires < 3:

        
        
        for i in range(len(bubble_list) - 1, -1, -1):
            move = (20 + score * 5) * delta_time
            bubble = bubble_list[i]
            flag = True
            if bubble['x'] < 170 and bubble['x'] > -200:
                new_x = bubble['x'] + move * fliper
                bubble['x'] = new_x
            elif bubble['x'] >= 170:
                fliper *= -1
                new_x = bubble['x'] + move * fliper
                bubble['x'] = new_x
            elif bubble['x'] <= -200:
                fliper *= -1
                new_x = bubble['x'] + move * fliper
                bubble['x'] = new_x
            else:
                print("in the else ")
    glutPostRedisplay()
############################################################################################################
def display():
    """Render the game display."""
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glClearColor(1, 1, 1, 0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    draw_bubble()
    glutSwapBuffers()

def init():
    """Initialize OpenGL settings."""
    global last_frame_time
    glClearColor(1, 1, 1, 0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-250, 250, -400, 400, -1, 1)
    last_frame_time = time.time()

glutInit()
glutInitWindowSize(W_WIDTH, W_HEIGHT)
glutInitWindowPosition(0, 0)
glutInitDisplayMode(GLUT_DEPTH | GLUT_DOUBLE | GLUT_RGB)
wind = glutCreateWindow(b"Shoot The Circles!")
init()
num_starting_bubbles = random.randint(3, 5)
for _ in range(num_starting_bubbles):
    new_bubble = create_bubble(bubble_list)
    bubble_list.append(new_bubble)
bubble_list.sort(key=bubble_x_position)
glutDisplayFunc(display)
glutIdleFunc(animate)
glutMainLoop()

def draw_points(x, y):
    glPointSize(5) 
    glBegin(GL_POINTS)
    glVertex2f(x,y) #jekhane show korbe pixel
    glEnd()

def iterate():
    glViewport(0, 0, 500, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()

    glutPostRedisplay()
    glutSwapBuffers()

############################################################
