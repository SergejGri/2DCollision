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
        self.m = random.uniform(1, 20)

        self.x1 = random.uniform(self.r, self.WIDTH - self.r)
        self.x2 = random.uniform(self.r, self.WIDTH - self.r)

        self.v1 = random.uniform(-50, 50)
        self.v2 = random.uniform(-50, 50)

        self.a1 = random.uniform(-1, 1)
        self.a2 = random.uniform(-1, 1)

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
        self.x1 +=  self.v1*dt
        self.x2 +=  self.v2*dt

    
    def check_walls():
        # simple collision check -- advanced check on todo
        if self.x1 - self.r < 0 or self.x1 + self.r > self.WIDTH:
            self.v1 *= -1
        if self.x2 - self.r < 0 or self.x2+ self.r > self.HEIGHT:
            self.v2 *= -1
