import random
import math
from GameConfigs import GameConfigs


class Circle:
    WIDTH = GameConfigs.width
    HEIGHT = GameConfigs.height

    def __init__(self):
        self.id = None
        self.r = random.uniform(15, 75)
        self.area = self.r * self.r * math.pi
        self.m = self.m = (self.r ** 2) * 0.1

        self.x = random.uniform(self.r, self.WIDTH - self.r)
        self.y = random.uniform(self.r, self.HEIGHT - self.r)

        self.vx = random.uniform(-400, 400)
        self.vy = random.uniform(-400, 400)

        self.ax = random.uniform(-1, 1)
        self.ay = random.uniform(-1, 1)

        self.color = random.choice(GameConfigs.PALETTE)
        self.neighbours = []


    def draw(self):
        pass

    def update_position(self, dt: float) -> None:
        self.vx += self.ax * dt
        self.vy += self.ay * dt
        
        self.x +=  self.vx*dt
        self.y +=  self.vy*dt

    
    def check_walls(self):
        b = GameConfigs.wall_bounciness

        # --- wall right ---
        if self.x + self.r > self.WIDTH:
            self.x = self.WIDTH -self.r
            self.vx *= -1 * b

        # --- wall left ---
        elif self.x - self.r < 0:
            self.x = self.r
            self.vx *= -1 * b
        
        # --- wall top ---
        if self.y - self.r < 0:
            self.y = self.r
            self.vy *= -1 * b
        
        # --- wall bottom ---
        elif self.y + self.r > self.HEIGHT:
            self.y = self.HEIGHT - self.r
            self.vy *= -1 *b