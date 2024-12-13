def plot_point(x, y):
    """Plot a single point using OpenGL."""
    from OpenGL.GL import glBegin, glVertex2f, glEnd, GL_POINTS
    glBegin(GL_POINTS)
    glVertex2f(x, y)
    glEnd()

def convert_to_zone0(x, y, zone):
    """Convert coordinates to zone 0 for line drawing algorithm."""
    zone_map = {
        0: (x, y),
        1: (y, x),
        2: (y, -x),
        3: (-x, y),
        4: (-x, -y),
        5: (-y, -x),
        6: (-y, x),
        7: (x, -y)
    }
    return zone_map[zone]

def convert_from_zone0(x, y, zone):
    """Convert coordinates from zone 0 back to original zone."""
    zone_map = {
        0: (x, y),
        1: (y, x),
        2: (-y, x),
        3: (-x, y),
        4: (-x, -y),
        5: (-y, -x),
        6: (y, -x),
        7: (x, -y)
    }
    return zone_map[zone]

def midpoint_line(x1, y1, x2, y2):
    """Midpoint line drawing algorithm."""
    dx = x2 - x1
    dy = y2 - y1
    zone = 0
    if abs(dx) > abs(dy):
        if dx >= 0 and dy >= 0:
            zone = 0
        elif dx < 0 and dy >= 0:
            zone = 3
        elif dx < 0 and dy < 0:
            zone = 4
        elif dx >= 0 and dy < 0:
            zone = 7
    else:
        if dx >= 0 and dy >= 0:
            zone = 1
        elif dx < 0 and dy >= 0:
            zone = 2
        elif dx < 0 and dy < 0:
            zone = 5
        elif dx >= 0 and dy < 0:
            zone = 6

    x1, y1 = convert_to_zone0(x1, y1, zone)
    x2, y2 = convert_to_zone0(x2, y2, zone)
    dx = x2 - x1
    dy = y2 - y1
    d = 2 * dy - dx
    incrE = 2 * dy
    incrNE = 2 * (dy - dx)
    x, y = x1, y1
    x0, y0 = convert_from_zone0(x, y, zone)
    plot_point(x0, y0)
    while x < x2:
        if d <= 0:
            d += incrE
            x += 1
        else:
            d += incrNE
            x += 1
            y += 1
        x0, y0 = convert_from_zone0(x, y, zone)
        plot_point(x0, y0)

def midpointcircle(radius, centerX=0, centerY=0):
    """Draw a circle using midpoint circle drawing algorithm."""
    from OpenGL.GL import glBegin, glVertex2f, glEnd, GL_POINTS
    glBegin(GL_POINTS)
    x = 0
    y = radius
    d = 1 - radius
    while y > x:
        glVertex2f(x + centerX, y + centerY)
        glVertex2f(x + centerX, -y + centerY)
        glVertex2f(-x + centerX, y + centerY)
        glVertex2f(-x + centerX, -y + centerY)
        glVertex2f(y + centerX, x + centerY)
        glVertex2f(y + centerX, -x + centerY)
        glVertex2f(-y + centerX, x + centerY)
        glVertex2f(-y + centerX, -x + centerY)
        if d < 0:
            d += 2 * x + 3
        else:
            d += 2 * x - 2 * y + 5
            y -= 1
        x += 1
    glEnd()

def convert_coordinate(x, y, window_width, window_height):
    """Convert screen coordinates to OpenGL coordinates."""
    a = x - (window_width / 2)
    b = (window_height / 2) - y
    return a, b