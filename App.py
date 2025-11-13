import pygame
import sys
from Circle import Circle
from GameConfigs import GameConfigs

pygame.init()



cfg = GameConfigs()
screen = pygame.display.set_mode((cfg.width, cfg.height))
pygame.display.set_caption(cfg.caption)
clock = pygame.time.Clock()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

def handle_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
    return True

def printer(radius, position, velocity):
    pass


def update_all(circles: object, dt: float):
    for c in circles:
        c.update_position(dt)
        c.check_walls()
    collision_handling(circles)


def colliding(c1: object, c2: object) -> bool:
    dx1 = c2.x1 - c1.x1
    dx2 = c2.x2 - c1.x2
    r_sum = c2.r + c1.r
    dist_square = dx1 * dx1 + dx2 * dx2
    return dist_square <= r_sum * r_sum


def collision_handling(circles: list, rho: float):
    if rho is None:
        rho = 1.0

    n = len(circles)
    for i in range(n):
        for j in range(i+1, n):
            c1 = circles[i]
            c2 = circles[j]
            if colliding(c1, c2):
                calc_collision(c1, c1, rho)


def calc_collision(circle1: object, circle2: object, rho: float) -> None:
    pass


def draw_line():
    pass


def draw_all(objects, screen):
    screen.fill(WHITE)
    for obj in objects:
        pygame.draw.circle(screen, obj.color, (obj.x1, obj.x2), obj.r)
    pygame.display.flip()
    

dt = clock.tick(140) / 1000.0

circles = []
for i in range(cfg.num_of_circles):
    c = Circle()
    c.id = i
    circles.append(c)


running = True
while running:
    running = handle_events()
    draw_all(circles, screen)
    update_all(circles, dt)

pygame.quit()
sys.exit()



