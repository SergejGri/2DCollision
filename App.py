import pygame
import sys
from Circle import Circle

pygame.init()
WIDTH, HEIGHT = 1080, 720
VERBOSE = False
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("XXX")
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

def update_all(objects, dt):
    for obj in objects:
        obj.update(dt)

def draw_all(objects, screen):
    screen.fill(WHITE)
    font = pygame.font.Font(None, 34)  # 'None' = default pygame font
    for obj in objects:
        if VERBOSE:
            text_surface = font.render(f"r: {round(obj.r, 3)}\n pos: ({round(obj.pos[0])} | {round(obj.pos[1])})", True, BLACK)  # text, antialias, color
            text_x = 20
            text_y = 20
            screen.blit(text_surface, (text_x, text_y))
        pygame.draw.circle(screen, obj.color, (obj.pos[0], obj.pos[1]), obj.r)
    pygame.display.flip()
    

dt = clock.tick(140) / 1000.0

circles = []
for i in range(10):
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



