import pygame
import random
import sys
import math
from Circle import Circle
from GameConfigs import GameConfigs

pygame.init()
cfg = GameConfigs()
screen = pygame.display.set_mode((cfg.width, cfg.height))
pygame.display.set_caption(cfg.caption)
font = pygame.font.SysFont(cfg.font, cfg.font_size)

clock = pygame.time.Clock()
counter = 0
rho = cfg.rho

HEIGHT = cfg.height
WIDTH = cfg.width

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (245, 245, 245)



def handle_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
    return True


def update_all(circles: object, dt: float):
    for c in circles:
        c.update_position(dt)
        c.check_walls()
    collision_handling(circles)


def colliding(c1: object, c2: object) -> bool:
    dx = c2.x - c1.x
    dy = c2.y - c1.y
    r_sum = c2.r + c1.r
    dist_square = dx * dx + dy * dy
    return dist_square <= r_sum * r_sum


def collision_handling(circles: list):
    global counter
    n = len(circles)
    for i in range(n):
        for j in range(i+1, n):
            c1 = circles[i]
            c2 = circles[j]
            if colliding(c1, c2):
                counter += 1
                calc_collision(c1, c2, rho)
    update_position(circles, dt)


def update_position(circle: object, dt: float):
    for i, c in enumerate(circles):
        c.x +=  c.vx*dt
        c.y +=  c.vy*dt


def calc_collision(circle1: object, circle2: object, rho: float) -> None:
    c1, c2 = circle1, circle2
    m1, m2 = c1.m, c2.m
    M = c1.m + c2.m
    
    dx = c2.x - c1.x
    dy = c2.y - c1.y
    dist = math.hypot(dx, dy)
    if dist <= 1e-5:
        return
    
    nx = dx / dist
    ny = dy / dist
    
    # A dot product with a unit vector gives a scalar component along 
    # that direction (m/s or px/s).
    rel_vx = c1.vx - c2.vx
    rel_vy = c1.vy - c2.vy
    vn = rel_vx * nx + rel_vy * ny

    j = -(1.0 + rho) * vn / (1.0 / m1 + 1.0 / m2)

    impulse_x = j * nx
    impulse_y = j * ny

    c1.vx += impulse_x / m1
    c1.vy += impulse_y / m1
    c2.vx -= impulse_x / m2
    c2.vy -= impulse_y / m2


def draw_all(objects, screen):
    screen.fill(GREY)
    for obj in objects:
        pygame.draw.circle(screen, obj.color, (obj.x, obj.y), obj.r)
    screen.blit(printer(), (30, 30))
    pygame.display.flip()
    

def create_circles(circles):
    for i in range(cfg.num_of_circles):
        c = Circle()
        c.id = i
        if i != 0 and overlapping(c, circles): 
                c.x, c.y = rdm_except(c)
        circles.append(c)
    return circles


def rdm_except(c):
    initial_x = c.x
    initial_y = c.y
    while True:
        c.x = random.uniform(c.r, c.WIDTH - c.r)
        c.y = random.uniform(c.r, c.HEIGHT - c.r)
        if c.x * 2 > initial_x and c.y * 2 > initial_y:
            return c.x, c.y


def overlapping(c, circles) -> bool:
    for other in circles:
        dx  = c.x - other.x
        dy  = c.y - other.y
        if dx * dx + dy * dy <= (c.r + other.r)**2:
            print(f"c: {c.id} and other: {other.id} overlapp")
            return True
    return False


def check_direction():
    # if vx has not y componen or vy no x conponent -> parallel motion to walls
    pass

def printer():
    text = font.render(f"Count: {counter}", True, BLACK)
    return text


dt = clock.tick(140) / 1000.0
circles: list[Circle] = []
create_circles(circles)

running = True
while running:
    running = handle_events()
    draw_all(circles, screen)
    update_all(circles, dt)
    

pygame.quit()
sys.exit()



