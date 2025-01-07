from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random
import time
from drawing_algorithms import midpointcircle
from maze_points import get_maze_points

# Window dimensions
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

# Maze points
maze_points = get_maze_points()

# Bubble list
bubble_list = []

# Level
level = 1

# Box position
box_x = 0
box_y = 0

# Last frame time
last_frame_time = 0

def plot_point(x, y):
    glBegin(GL_POINTS)
    glVertex2f(x, y)
    glEnd()

def draw_bubble():
    global bubble_list
    for bubble in bubble_list:
        glColor3f(bubble['color'][0], bubble['color'][1], bubble['color'][2])
        midpointcircle(bubble['r'], bubble['x'], bubble['y'])

def is_within_maze(x, y):
    """Check if the position is within the maze boundaries."""
    for i in range(len(maze_points)):
        x1, y1, x2, y2 = maze_points[i]
        if x1 == x2:  # Vertical line
            if x1 - 10 < x < x1 + 10 and min(y1, y2) < y < max(y1, y2):
                return False
        elif y1 == y2:  # Horizontal line
            if y1 - 10 < y < y1 + 10 and min(x1, x2) < x < max(x1, x2):
                return False
    return True

def create_bubble(existing_bubbles, inside_maze=True):
    """Generate a random position for a bubble."""
    while True:
        if inside_maze:
            x = random.randint(-WINDOW_WIDTH // 2 + 20, WINDOW_WIDTH // 2 - 20)
            y = random.randint(-WINDOW_HEIGHT // 2 + 20, WINDOW_HEIGHT // 2 - 20)
            if is_within_maze(x, y):
                continue
        else:
            x = random.choice([-WINDOW_WIDTH // 2 + 20, WINDOW_WIDTH // 2 - 20])
            y = random.choice([-WINDOW_HEIGHT // 2 + 20, WINDOW_HEIGHT // 2 - 20])
        
        if not check_bubble_overlap(x, y, existing_bubbles):
            bubble = {
                'x': x,
                'y': y,
                'r': 10,
                'color': [random.random(), random.random(), random.random()],
                'dx': random.choice([-1, 1]) * random.uniform(0.5, 1.5),
                'dy': random.choice([-1, 1]) * random.uniform(0.5, 1.5)
            }
            return bubble

def check_bubble_overlap(x, y, other_bubbles):
    for other in other_bubbles:
        distance = ((x - other['x']) ** 2 + (y - other['y']) ** 2) ** 0.5
        if distance < 20:
            return True
    return False

def update_bubbles():
    global bubble_list, box_x, box_y, last_frame_time
    current_time = time.time()
    delta_time = current_time - last_frame_time
    last_frame_time = current_time

    for bubble in bubble_list:
        dx = box_x - bubble['x']
        dy = box_y - bubble['y']
        distance = (dx ** 2 + dy ** 2) ** 0.5
        if distance > 0:
            bubble['x'] += (dx / distance) * bubble['dx'] * delta_time
            bubble['y'] += (dy / distance) * bubble['dy'] * delta_time

        if bubble['x'] < -WINDOW_WIDTH // 2 or bubble['x'] > WINDOW_WIDTH // 2:
            bubble['dx'] *= -1
        if bubble['y'] < -WINDOW_HEIGHT // 2 or bubble['y'] > WINDOW_HEIGHT // 2:
            bubble['dy'] *= -1

def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    draw_bubble()
    glutSwapBuffers()

def animate():
    update_bubbles()
    glutPostRedisplay()

def init():
    global last_frame_time
    glClearColor(1, 1, 1, 1)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(-WINDOW_WIDTH // 2, WINDOW_WIDTH // 2, -WINDOW_HEIGHT // 2, WINDOW_HEIGHT // 2)
    last_frame_time = time.time()

def main():
    global bubble_list, level
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(WINDOW_WIDTH, WINDOW_HEIGHT)
    glutCreateWindow(b"Bubble Maze")
    init()
    num_bubbles = 3 + min(level - 1, 4) * 2 + max(level - 5, 0)
    for _ in range(num_bubbles):
        inside_maze = _ != 0  # First bubble outside, others inside
        new_bubble = create_bubble(bubble_list, inside_maze)
        bubble_list.append(new_bubble)
    glutDisplayFunc(display)
    glutIdleFunc(animate)
    glutMainLoop()

if __name__ == "__main__":
    main()
