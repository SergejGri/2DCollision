import random
from GameConfigs import GameConfigs


class Circle:
    WIDTH = GameConfigs.width
    HEIGHT = GameConfigs.height

    def __init__(self):
        self.id = None
        self.WIDTH = GameConfigs.width
        self.HEIGHT = GameConfigs.height
        self.r = random.uniform(25, 60)
        self.m = random.uniform(5, 20)

        self.x = random.uniform(self.r, self.WIDTH - self.r)
        self.y = random.uniform(self.r, self.HEIGHT - self.r)

        self.vx = random.uniform(-27, 27)
        self.vy = random.uniform(-27, 27)

        self.ax = random.uniform(-1, 1)
        self.ay = random.uniform(-1, 1)

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
        self.x +=  self.vx*dt
        self.y +=  self.vy*dt

    
    def check_walls(self):
        # simple collision check -- advanced check on todo
        if self.x - self.r < 0 or self.x + self.r > self.WIDTH:
            self.vx *= -1
        if self.y - self.r < 0 or self.y+ self.r > self.HEIGHT:
            self.vy *= -1