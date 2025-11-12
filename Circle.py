import random
import math
import pygame
from GameConfigs import GameConfigs


class Circle:
    WIDTH = GameConfigs.width
    HEIGHT = GameConfigs.height

    def __init__(self):
        self.id = None
        self.WIDTH = GameConfigs.width
        self.HEIGHT = GameConfigs.height
        self.r = random.uniform(15, 45)
        self.pos = pygame.math.Vector2(
            random.uniform(self.r, self.WIDTH - self.r),
            random.uniform(self.r, self.HEIGHT - self.r))
        self.v = pygame.math.Vector2(
            random.uniform(-50, 50),
            random.uniform(-50, 50)
        )
        self.a = pygame.math.Vector2(
            random.uniform(-1, 1),
            random.uniform(-1, 1)
        )
        self.color = self._random_color()
        self.neighbours = []


    def _random_color(self):
        return (
            # to-do implement color palette 
            random.uniform(0, 240), 
            random.uniform(0, 240), 
            random.uniform(0, 240)
            )

    def draw(self):
        pass

    def update_position(self, dt: float) -> None:
        self.pos[0] +=  self.v[0]*dt
        self.pos[1] +=  self.v[1]*dt

    
    def check_walls(self):
        # simple collision check -- advanced check on todo
        if self.pos[0] - self.r < 0 or self.pos[0] + self.r > self.WIDTH:
            self.v[0] *= -1
        if self.pos[1] - self.r < 0 or self.pos[1] + self.r > self.HEIGHT:
            self.v[1] *= -1

    def check_balls(self, other: list):
        # nearest neighbor check
        dist = math.dist((other[1], self.pos[1]) (other[0], self.pos[0]))