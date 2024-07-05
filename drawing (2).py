import pygame as py

py.init()

fps = 60
timer = py.time.Clock()
WIDTH = 800
HEIGHT = 600
screen = py.display.set_mode((WIDTH, HEIGHT))
active_size = 0
active_color = 'white'
painting = []
white = (255, 255, 255)
bg_color = white
py.display.set_caption("Painting")

run = True
erasing = False

def draw_menu(size, color, erasing):
    py.draw.rect(screen, 'gray', [0, 0, WIDTH, 70])  # draw rect is (rectangle )
    py.draw.line(screen, 'black', (0, 70), (WIDTH, 70))

    xl_brush = py.draw.rect(screen, 'black', [10, 10, 50, 50])
    py.draw.circle(screen, 'white', (35, 35), 20)  # draw circle 
    l_brush = py.draw.rect(screen, 'black', [70, 10, 50, 50])
    py.draw.circle(screen, 'white', (95, 35), 15)
    m_brush = py.draw.rect(screen, 'black', [130, 10, 50, 50])
    py.draw.circle(screen, 'white', (155, 35), 10)
    s_brush = py.draw.rect(screen, 'black', [190, 10, 50, 50])
    py.draw.circle(screen, 'white', (215, 35), 5)

    brush_list = [xl_brush, l_brush, m_brush, s_brush]

    if size == 20:
        py.draw.rect(screen, 'purple', [10, 10, 50, 50], 3)
    elif size == 15:
        py.draw.rect(screen, 'green', [70, 10, 50, 50], 3)
    elif size == 10:
        py.draw.rect(screen, 'red', [130, 10, 50, 50], 3)
    elif size == 5:
        py.draw.rect(screen, 'yellow', [190, 10, 50, 50], 3)

    py.draw.circle(screen, color, (400, 35), 30)
    py.draw.circle(screen, 'dark gray', (400, 35), 30, 3)

    blue = py.draw.rect(screen, (0, 0, 255), [WIDTH - 35, 10, 25, 25])
    red = py.draw.rect(screen, (255, 0, 0), [WIDTH - 35, 35, 25, 25])
    green = py.draw.rect(screen, (0, 255, 0), [WIDTH - 60, 10, 25, 25])
    yellow = py.draw.rect(screen, (255, 255, 0), [WIDTH - 60, 35, 25, 25])
    teal = py.draw.rect(screen, (0, 255, 255), [WIDTH - 85, 10, 25, 25])
    purple = py.draw.rect(screen, (255, 0, 255), [WIDTH - 85, 35, 25, 25])
    white = py.draw.rect(screen, (0, 0, 0), [WIDTH - 110, 10, 25, 25])
    black = py.draw.rect(screen, (255, 255, 255), [WIDTH - 110, 35, 25, 25])

    color_list = [blue, red, green, yellow, teal, purple, white, black]
    rgb_list = [(0, 0, 255), (255, 0, 0), (0, 255, 0), (255, 255, 0), (0, 255, 255), (255, 0, 255), (0, 0, 0), (255, 255, 255)]

    # Draw the eraser button
    eraser_button = py.draw.rect(screen, 'white', [WIDTH - 200, 10, 50, 50])
    py.draw.line(screen, 'black', (WIDTH - 150, 10), (WIDTH - 200, 60), 3)
    py.draw.line(screen, 'black', (WIDTH - 150, 60), (WIDTH - 200, 10), 3)

    if erasing:
        py.draw.rect(screen, 'red', [WIDTH - 200, 10, 50, 50], 3)

    return brush_list, color_list, rgb_list, eraser_button

def draw_painting(painting):
    for i in range(len(painting)):
        py.draw.circle(screen, painting[i][0], painting[i][1], painting[i][2])

while run:
    timer.tick(fps)
    screen.fill(white)
    left_click = py.mouse.get_pressed()[0]
    press = py.mouse.get_pos()

    if left_click and press[1] > 70:
        color = bg_color if erasing else active_color
        painting.append((color, press, active_size))

    draw_painting(painting)

    if press[1] > 70:
        py.draw.circle(screen, bg_color if erasing else active_color, press, active_size)
    brushes, colors, rgbs, eraser_button = draw_menu(active_size, active_color, erasing)

    for event in py.event.get():
        if event.type == py.QUIT:
            run = False

        if event.type == py.MOUSEBUTTONDOWN:
            for i in range(len(brushes)):
                if brushes[i].collidepoint(event.pos):  # x&y coordinate
                    active_size = 20 - (i * 5)
                    erasing = False  # Reset erasing when selecting a brush
            for i in range(len(colors)):
                if colors[i].collidepoint(event.pos):  # x&y coordinate
                    active_color = rgbs[i]
                    erasing = False  # Reset erasing when selecting a color

            # Check for eraser button selection
            if eraser_button.collidepoint(event.pos):
                erasing = True

    py.display.flip()

py.quit()
