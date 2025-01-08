from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GLUT.fonts import GLUT_BITMAP_HELVETICA_18
import sys
import random
import time
from drawing_algorithms import midpoint_line, convert_coordinate, midpointcircle
from maze_points import get_maze_points
from CG_calc import calculate_cg
from intro import intro_main
from outro import exit_game, outro_main
maze_points = get_maze_points()
import math

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

bubble_list = []
level = 1
total_cg = 4
semester_cg = 4

box_size = 15

stickman_x = 0
stickman_y = 0

# top_maze = [-340, 100, 350, 100]
# bottom_maze = [-340, 200, -220, 200]
# right_maze = [350, 160, 350, -200]
# left_maze = [-340, -200, -340, 200]

def plot_point(x, y):
    glBegin(GL_POINTS)
    glVertex2f(x, y)
    glEnd()

#box
def draw_box(x, y, size):
    half_size = size // 2
    midpoint_line(x - half_size, y - half_size, x + half_size, y - half_size)  # Bottom
    midpoint_line(x + half_size, y - half_size, x + half_size, y + half_size)  # Right
    midpoint_line(x + half_size, y + half_size, x - half_size, y + half_size)  # Top
    midpoint_line(x - half_size, y + half_size, x - half_size, y - half_size)  # Left

#maze
def draw_maze():
    global maze_points
    glColor3f(0, 0, 0)
    for i in range(len(maze_points)):
        midpoint_line(maze_points[i][0], maze_points[i][1], maze_points[i][2], maze_points[i][3])

#bubble
def draw_bubble():
    global bubble_list
    for bubble in bubble_list:
        glColor3f(bubble['color'][0], bubble['color'][1], bubble['color'][2])
        midpointcircle(bubble['r'], bubble['x'], bubble['y'])

#stickman
def draw_stickman(x, y):
    head_radius = 10
    body_length = 30
    arm_length = 20
    leg_length = 20

    # Draw head
    midpointcircle(head_radius, x, y + body_length)

    # Draw body
    midpoint_line(x, y, x, y + body_length)

    # Draw arms
    midpoint_line(x - arm_length, y + body_length - 10, x + arm_length, y + body_length - 10)

    # Draw legs
    midpoint_line(x, y, x - leg_length, y - leg_length)
    midpoint_line(x, y, x + leg_length, y - leg_length)

# score
def draw_score():
    global total_cg, level, semester_cg
    glColor3f(0, 0, 0)
    glRasterPos2f(-380, 280)
    for ch in f"Total CG: {total_cg:.2f}":
        glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, ord(ch))
    glRasterPos2f(-380, 250)
    for ch in f"Semester: {level}":
        glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, ord(ch))
    glRasterPos2f(-380, 220)
    for ch in f"CG: {semester_cg:.2f}":
        glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, ord(ch))

def draw_buttons():
    # quit
    glPointSize(2)
    glColor3f(0.7, 0.1, 0.1)
    midpoint_line(370, 270, 390, 290)
    midpoint_line(370, 290, 390, 270)

   #restart 
    glPointSize(2)
    glColor3f(0.5, 0.8, 0.4)
    midpoint_line(335, 280, 360, 280)
    glPointSize(2)
    midpoint_line(335, 280, 342, 285)
    midpoint_line(335, 280, 342, 275)

def display():
    """Display callback for GLUT."""
    glClear(GL_COLOR_BUFFER_BIT)
    draw_maze()
    draw_buttons()
    glColor3f(1, 0, 0)  # box 
    draw_box(box_x, box_y, box_size) 
    draw_bubble()  
    glColor3f(0, 0, 1)  # stickman color (blue)
    draw_stickman(stickman_x, stickman_y)  
    draw_score()  
    glFlush()


def reshape(width, height):
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(-WINDOW_WIDTH // 2, WINDOW_WIDTH // 2, -WINDOW_HEIGHT // 2, WINDOW_HEIGHT // 2)
    glMatrixMode(GL_MODELVIEW)


#bhai eita fix kor. bishal boro gap maze and box er moddhe
def is_within_maze(x, y):
    
    for i in range(len(maze_points)):
        x1, y1, x2, y2 = maze_points[i]
        if x1 == x2:  # Vertical line
            if x1 - 5 < x < x2 + 5 and min(y1, y2) < y < max(y1, y2):
                return False
        elif y1 == y2:  # Horizontal line
            if y1 - 5 < y < y1 + 5 and min(x1, x2) < x < max(x1, x2):
                return False
    return True

# need fix. animated bubble lagbe for level 3,8,11. Bamboo shaped er
def create_bubble(existing_bubbles, inside_maze=True):
    """Generate a random position for a bubble."""
    while True:
        r = 10
        is_special_object = False
        levels = [3, 8, 11]
        global level
        if level in levels:
            is_special_object = random.random() < 0.50
        
        if is_special_object:
            r = 20
        
        if inside_maze:
            x = random.randint(-WINDOW_WIDTH // 2 + 20, WINDOW_WIDTH // 2 - 20)
            y = random.randint(-WINDOW_HEIGHT // 2 + 20, WINDOW_HEIGHT // 2 - 20)
            if not is_within_maze(x, y):
                continue
        else:
            x = random.choice([-WINDOW_WIDTH // 2 + 20, WINDOW_WIDTH // 2 - 20])
            y = random.choice([-WINDOW_HEIGHT // 2 + 20, WINDOW_HEIGHT // 2 - 20])
        
        if not check_bubble_overlap(x, y, existing_bubbles):
            bubble = {
                'x': x,
                'y': y,
                'r': r,
                'color': [random.random(), random.random(), random.random()],
                'dx': random.choice([-1, 1]) * random.uniform(0.5, 1.5),
                'dy': random.choice([-1, 1]) * random.uniform(0.5, 1.5), 
                'is_special_object': is_special_object
            }
            return bubble


def check_bubble_overlap(x, y, other_bubbles):
    for other in other_bubbles:
        distance = ((x - other['x']) ** 2 + (y - other['y']) ** 2) ** 0.5
        if distance < 20:
            return True
    return False


def update_bubbles():
    global bubble_list
    for bubble in bubble_list:
        bubble['x'] += bubble['dx']
        bubble['y'] += bubble['dy']
        if bubble['x'] < -WINDOW_WIDTH // 2 or bubble['x'] > WINDOW_WIDTH // 2:
            bubble['dx'] *= -1
        if bubble['y'] < -WINDOW_HEIGHT // 2 or bubble['y'] > WINDOW_HEIGHT // 2:
            bubble['dy'] *= -1

def remove_special_object():
    global level
    global bubble_list
    if level not in [3, 8, 11]:
            for objects in bubble_list:
                if objects['is_special_object']:
                    bubble_list.remove(objects)
def special_keys(key, x, y):
    global box_x, box_y, level, stickman_x, stickman_y, semester_cg, total_cg
    move_step = 10 
    new_x, new_y = box_x, box_y

    if key == GLUT_KEY_UP:       
        new_y += move_step
    elif key == GLUT_KEY_DOWN:   
        new_y -= move_step
    elif key == GLUT_KEY_LEFT:  
        new_x -= move_step
    elif key == GLUT_KEY_RIGHT:  
        new_x += move_step

    # Check if the new position is within the maze boundaries and window boundaries
    if is_within_maze(new_x, new_y) and -WINDOW_WIDTH // 2 <= new_x <= WINDOW_WIDTH // 2 and -WINDOW_HEIGHT // 2 <= new_y <= WINDOW_HEIGHT // 2:
        box_x, box_y = new_x, new_y

    # Check if the box touches the stickman
    if abs(box_x - stickman_x) < box_size and abs(box_y - stickman_y) < box_size:
        # Generate new random positions for the stickman and the box
        box_x, box_y = get_random_position()
        stickman_x, stickman_y = get_random_position_for_stickman()

        # need fix. eikhane korte chaisilam hoi nai.
        # if level % 3 == 0:
        #     new_bubble = create_bubble(bubble_list, inside_maze=True)
        #     bubble_list.append(new_bubble)

        # Update total CG
        remove_special_object()
        total_cg = calculate_cg(semester_cg, level, total_cg)
        #when the level is not 3, 8 or 11 remove the bubble that have 
        #is_special_object = True
        # 
        remove_special_object()

        level += 1
        iterate = level
        for i in range(iterate):
            new_bubble = create_bubble(bubble_list, inside_maze=True)
            bubble_list.append(new_bubble)
        remove_special_object()
        semester_cg = 4  
        print(f"Level increased to {level}")

        
        if level == 11:
            outro_main(level, total_cg)

    #if the box touches a bubble
    for bubble in bubble_list:
        if abs(box_x - bubble['x']) < box_size and abs(box_y - bubble['y']) < box_size:
            reduction = random.uniform(0.1, 0.5)
            semester_cg -= reduction
            print(f"Bubble hit! CG reduced by {reduction:.2f}. Current CG: {semester_cg:.2f}")

    
    glutPostRedisplay()

def restart_game():
    global box_x, box_y, bubble_list, level, stickman_x, stickman_y, total_cg, semester_cg
    box_x, box_y = get_random_position()
    stickman_x, stickman_y = get_random_position_for_stickman()
    bubble_list = []
    level = 1
    total_cg = 4
    semester_cg = 4
    for _ in range(6):
        new_bubble = create_bubble(bubble_list, inside_maze=True)
        bubble_list.append(new_bubble)
    glutPostRedisplay()


def animate_bubble():
    global bubble_list
    for bubble in bubble_list:
        bubble['x'] += bubble['dx']
        bubble['y'] += bubble['dy']
        if bubble['x'] < -WINDOW_WIDTH // 2 or bubble['x'] > WINDOW_WIDTH // 2:
            bubble['dx'] *= -1
        if bubble['y'] < -WINDOW_HEIGHT // 2 or bubble['y'] > WINDOW_HEIGHT // 2:
            bubble['dy'] *= -1

    glutPostRedisplay()

def keyboardListener(key, _, __):
    if key == b'r':
        # Restart the game
        print("Restarting Game...")
        restart_game()
        
    elif key == b'q':
        # Quit the game
        print("Goodbye!")
        exit_game()
    glutPostRedisplay()

def mouseListener(button, state, x, y):
    if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
        # Convert screen coordinates to OpenGL coordinates
        ogl_x = x - WINDOW_WIDTH // 2
        ogl_y = WINDOW_HEIGHT // 2 - y

        if 335 <= ogl_x <= 360 and 270 <= ogl_y <= 290:
            print("Restarting Game...")
            restart_game()
        # Check if the "quit" button is clicked
        elif 370 <= ogl_x <= 390 and 270 <= ogl_y <= 290:
            print("Goodbye!")
            exit_game()
    glutPostRedisplay()

def get_random_position():
    """Get a random position within the maze boundaries."""
    while True:
        x = random.randint(-WINDOW_WIDTH // 2 + box_size, WINDOW_WIDTH // 2 - box_size)
        y = random.randint(-WINDOW_HEIGHT // 2 + box_size, WINDOW_HEIGHT // 2 - box_size)
        if is_within_maze(x, y):
            return x, y

# need fix. stickman line er moddhe generate hoye jai
def get_random_position_for_stickman():
    while True:
        x = random.randint(-340, 350)
        y = random.randint(-200, 200)
        if is_within_maze(x, y):
            return x, y



def start_game():
    """Main function to set up OpenGL with GLUT."""
    global box_x, box_y, bubble_list, level, stickman_x, stickman_y
    box_x, box_y = get_random_position()
    stickman_x, stickman_y = get_random_position_for_stickman()
    
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(WINDOW_WIDTH, WINDOW_HEIGHT)
    glutCreateWindow(b"Midpoint Maze Drawing")
    glClearColor(1.0, 1.0, 1.0, 1.0)  # Set background color to white
    glColor3f(0.0, 0.0, 0.0)          # Set drawing color to black
    glPointSize(2)                    # Set point size
    glutDisplayFunc(display)
    glutReshapeFunc(reshape)
    glutSpecialFunc(special_keys)
    glutMouseFunc(mouseListener)  # Register mouse event handler
    glutKeyboardFunc(keyboardListener)   # Register arrow key event handler
    glutIdleFunc(animate_bubble)  # Use animate_bubble for idle function

    # need fix. Generate 10 bubbles initially. do you need more bubble?
    for _ in range(6):
        new_bubble = create_bubble(bubble_list, inside_maze=True)
        bubble_list.append(new_bubble)

    glutMainLoop()

if __name__ == "__main__":
    intro_main(start_game)
