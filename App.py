import pygame
import sys
import random
from Circle import Circle


pygame.init()
WIDTH, HEIGHT = 1080, 720
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("XXX")
WHITE = (255, 255, 255)


circles = []
for i in range(1):
    c = Circle()
    c.id = i
    circles.append(c)


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    

    screen.fill(WHITE)
    for c in circles:
        print("vor dem update")
        print(f"id: {c.id} Farbe: {c.color} x: {c.x_0} y: {c.y_0}")
        pygame.draw.circle(screen, c.color, (c.x_0, c.x_0), c.radius)
        pygame.display.flip()
        c.update()
        print(" ")
        print("nach dem update")
        print(f"id: {c.id} Farbe: {c.color} x: {c.x_0} y: {c.y_0}")
pygame.quit()
sys.exit()



