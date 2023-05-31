from time import sleep
import pygame

# GUI Setup
pygame.init()
pygame.display.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# create window
window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("N-Body Simulation")

sw2 = SCREEN_WIDTH / 2
sh2 = SCREEN_HEIGHT / 2

# mass: 0, name: 1, pos: 2, color: 3, raduis: 4
sun = [10000, "sun", [sw2, sh2], (255, 0, 0), 10]
earth = [100, "earth", [sw2 + 100, sh2], (0, 255, 0), 5]

planets = [sun, earth]


def update_simulation():
    pass


def draw_body(body):
    pygame.draw.circle(window, body[3], (body[2][0], body[2][1]), body[4])


def render_frame():
    for body in planets:
        draw_body(body)


should_be_running = True
while should_be_running:
    # handel events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            should_be_running = False

    # clear -> draw -> swap buffer
    window.fill((0, 0, 0))
    update_simulation()
    render_frame()
    pygame.display.flip()
    sleep(1 / 60)
