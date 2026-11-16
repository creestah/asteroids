import pygame, random
from logger import log_event
from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(
            screen,
            "white",
            self.position,
            self.radius,
            LINE_WIDTH,
        )

    def update(self, dt: float) -> None:
        self.position += self.velocity * dt

    def split(self) -> bool:
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return True
        else:
            log_event("asteroid_split")
            new_angle = random.uniform(0, 360)
            asteroid1_velocity = self.velocity.rotate(new_angle)
            asteroid2_velocity = self.velocity.rotate(-new_angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid1.velocity = asteroid1_velocity * 1.2
            asteroid2.velocity = asteroid2_velocity * 1.2
            return False

