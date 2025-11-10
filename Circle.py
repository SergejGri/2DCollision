import random
import math
import pygame

WIDTH = 1080
HEIGHT = 720

class Circle:
    def __init__(self):
        self.id = None
        self.r = random.uniform(15, 45)
        self.pos = pygame.math.Vector2(
            random.uniform(self.r, WIDTH - self.r),
            random.uniform(self.r, HEIGHT - self.r))
        self.v = pygame.math.Vector2(
            random.uniform(-50, 50),
            random.uniform(-50, 50)
        )
        self.a = pygame.math.Vector2(
            random.uniform(-1, 1),
            random.uniform(-1, 1)
        )
        self.color = self._random_color()


    def _random_color(self):
        return (
            # to-do implement color palette 
            random.uniform(0, 240), 
            random.uniform(0, 240), 
            random.uniform(0, 240)
            )

    def draw(self):
        pass

    def update(self, dt):
        self.pos[0] +=  self.v[0]*dt
        self.pos[1] +=  self.v[1]*dt
        self.check_walls()
        self.check_balls()

    
    def check_walls(self):
        # simple collision check -- advanced check on todo
        if self.pos[0] - self.r < 0 or self.pos[0] + self.r > WIDTH:
            self.v[0] *= -1
        if self.pos[1] - self.r < 0 or self.pos[1] + self.r > HEIGHT:
            self.v[1] *= -1

    def check_balls(self):
        pass