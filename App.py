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

def update_all(objects, dt: float):
    for obj in objects:
        obj.update_position(dt)
        obj.check_walls()
        #obj.check_balls()
        check_balls(circles)

def check_balls(circles: list):
    for n in range(len(circles)-1):
        dx = circles[n+1].pos[0] - circles[n].pos[0]
        dy = circles[n+1].pos[1] - circles[n].pos[1]

        distance_sq = dx * dx + dy * dy
        radius_sum = circles[n+1].r + circles[n+1].r
        if distance_sq <= radius_sum * radius_sum:
            print("boing!")
            print(" ")
    


def draw_line():
    pass


def draw_all(objects, screen):
    screen.fill(WHITE)
    for obj in objects:
        pygame.draw.circle(screen, obj.color, (obj.pos[0], obj.pos[1]), obj.r)
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



