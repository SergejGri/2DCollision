import random
import math

WIDTH = 1080
HEIGHT = 720

class Circle:
    def __init__(self):
        self.id = None
        self.radius = self.radius()
        self.x_0, self.y_0 = self.start_position(self.radius)
        self.v_x = random.uniform(-0.001, 0.001)
        self.v_y = random.uniform(-0.001, 0.001)
        #self.a_0_x, self.a_0_y = self.acceleration()
        self.color = self.color()

    def radius(self) -> float:
        return random.uniform(5, 50)

    def start_position(self, r: float) -> tuple[float, float]:
        x = random.uniform(r, WIDTH - r)
        y = random.uniform(r, HEIGHT - r)
        return x,y
    
    def acceleration(self) -> float:
        a_x = random.uniform(-1, 1)
        a_y = random.uniform(-1, 1)
        return a_x,a_y
    
    def trajectory(self, a_x, a_y, v_x, v_y, t):
        x = 0.5*a_x*t*t+v_x*t
        y = 0.5*a_y*t*t+v_y*t
        return x, y

    def color(self) -> tuple:
        return (random.uniform(5, 255), random.uniform(5, 255), random.uniform(5, 255))

    def update(self):
        angle = random.uniform(0, 2 * math.pi)
        self.v_x = math.cos(angle) * self.x_0
        self.v_y = math.sin(angle) * self.y_0
        self.x_0 += self.v_x
        self.y_0 += self.v_y

        
        

        if self.x_0 - self.radius < 0 or self.x_0 + self.radius > WIDTH:
            self.v_x *= -1  # Richtung umdrehen
        if self.y_0 - self.radius < 0 or self.y_0 + self.radius > HEIGHT:
            self.v_y *= -1