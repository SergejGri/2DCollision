import pygame
import random
import sys
import math
from Circle import Circle
from GameConfigs import GameConfigs

pygame.init()

screen = pygame.display.set_mode((GameConfigs.width, GameConfigs.height))
pygame.display.set_caption(GameConfigs.caption)
font = pygame.font.SysFont(GameConfigs.font, GameConfigs.font_size)

clock = pygame.time.Clock()
counter = 0
rho = GameConfigs.rho

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


def handle_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
    return True


def update_all(circles: object, dt: float):
    sub_step = dt / GameConfigs.sub_steps
    for _ in range(GameConfigs.sub_steps):
        for c in circles:
            c.update_position(sub_step)
            c.check_walls()
    
    collision_handling(circles)


def colliding(c1: object, c2: object) -> bool:
    r_sum = c2.r + c1.r
    return _dist_square(c1, c2) <= r_sum * r_sum


def _dist_square(c1: object, c2: object) -> float:
    dx = c2.x - c1.x
    dy = c2.y - c1.y
    return dx * dx + dy * dy


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


def calc_collision(circle1: object, circle2: object, rho: float) -> None:
    c1, c2 = circle1, circle2
    
    dx = c2.x - c1.x
    dy = c2.y - c1.y
    dist = math.hypot(dx, dy)

    if dist == 0:
        return
    
    nx = dx / dist
    ny = dy / dist
    
    overlap = (c1.r + c2.r) - dist

    if overlap > 0:
        _fix_overlap(c1, c2, nx, ny, overlap)
    _apply_impulse(c1, c2, nx, ny, rho)


def _fix_overlap(c1: object, c2: object, nx: float, ny: float, overlap: float) -> None:
    move_x = nx * (overlap / 2.0)
    move_y = ny * (overlap / 2.0)

    c1.x -= move_x
    c1.y -= move_y
    c2.x += move_x
    c2.y += move_y


def _apply_impulse(c1: object, c2: object, nx: float, ny: float, rho: float) -> None:
    # A dot product with a unit vector gives a scalar component along 
    # that direction (m/s or px/s).

    # relative velocity
    rel_vx = c1.vx - c2.vx
    rel_vy = c1.vy - c2.vy

    vn = rel_vx * nx + rel_vy * ny
    # if normal velocity greater 0 -> circles moving opposite direction
    if vn > 0:
        return

    m1, m2 = c1.m, c2.m
    j = -(1.0 + rho) * vn / (1.0 / m1 + 1.0 / m2)
    impulse_x = j * nx
    impulse_y = j * ny

    c1.vx += impulse_x / m1
    c1.vy += impulse_y / m1
    c2.vx -= impulse_x / m2
    c2.vy -= impulse_y / m2


def draw_all(objects: list, screen) -> None:
    screen.fill(GameConfigs.background_color)
    for obj in objects:
        pygame.draw.circle(screen, obj.color, (obj.x, obj.y), obj.r)
    screen.blit(printer(), (30, 30))
    pygame.display.flip()
    

def create_circles(circles: list) -> list:
    max_attempts = 500
    while len(circles) < GameConfigs.num_of_circles:
        created = False
        attempts = 0
        while not created and attempts < max_attempts:
            new_circle = Circle()
            overlap = False
            for other in circles:
                dx = new_circle.x - other.x
                dy = new_circle.y - other.y
                if dx * dx + dy * dy < (new_circle.r + other.r + 5)**2:
                    overlap = True
                    break
            
            if not overlap:
                circles.append(new_circle)
                created = True
            else:
                attempts += 1
        
        if not created:
            print("Seems like the number of circles is to high...")
            break

    return circles


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
    #text = font.render(f"Count: {counter}", True, BLACK)
    return text


def printer2(base_fn):
    def enhanced_fn(*args):
        text = text
        text = font.render(f"Count: {counter}", True, BLACK)
        return text



circles: list[Circle] = []
create_circles(circles)

running = True
while running:
    dt = clock.tick(GameConfigs.fps) / 1000.0
    running = handle_events()
    draw_all(circles, screen)
    update_all(circles, dt)
    

pygame.quit()
sys.exit()



