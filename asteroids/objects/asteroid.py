import pygame

from math import radians
from math import sin
from math import cos
from math import atan2

from random import random

from pygame.sprite import Sprite
from asteroids.interfaces.updateable import Updateable

class Asteroid(Sprite, Updateable): 
    def __init__(self, position: pygame.Vector2) -> None:
        super().__init__()
        Updateable.__init__(self)

        self.size = pygame.Vector2(100, 100) 
        self.surface = pygame.Surface(
            size = self.size,
            flags = pygame.SRCALPHA
        )
        self.rect = self.surface.get_rect()

        self.position = position

        self.velocity = 100
        self.velocityHat = pygame.Vector2(0, 0)

        self.draw()

    def draw(self) -> None:
        points = [pygame.Vector2(random() * 100, random() * 100) for _ in range(5)]

        def getCenter(points: list[pygame.Vector2]) -> pygame.Vector2:
            start = pygame.Vector2(0, 0)

            return sum(points, start) / len(points)

        center = getCenter(points)

        def angle(point: pygame.Vector2) -> float:
            v = point - center

            return atan2(v.y, v.x)
        
        points.sort(key = angle)

        pygame.draw.polygon(
            surface = self.surface, 
            color = "red", 
            points = points, 
            width = 1
        )

    def update(self, screen: pygame.Surface, dt: float) -> None:
        self.position += self.velocityHat * self.velocity * dt

        self.rect.center = self.position

        screen.blit(self.surface, self.rect)
