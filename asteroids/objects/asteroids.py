import pygame

from math import radians
from math import sin
from math import cos

from random import random

from pygame.sprite import Sprite
from asteroids.interfaces.updateable import Updateable

class Asteroids(Sprite, Updateable): 
    def __init__(self) -> None:
        super().__init__()
        Updateable.__init__(self)

        self.radius = 50
        self.surface = pygame.Surface(
            size = pygame.Vector2(2, 2) * self.radius
        )
        self.rect = self.surface.get_rect()

        self.position = pygame.Vector2(200, 200)

        self.velocity = 100
        self.velocityHat = self.randomDirection()

        self.draw()

    def randomDirection(self) -> pygame.Vector2:
        angle = radians(random() * 360)

        return pygame.Vector2(
            cos(angle), 
            sin(angle)
        )

    def draw(self) -> None:
        pygame.draw.circle(
            surface = self.surface, 
            color = "red", 
            center = self.rect.center, 
            radius = self.radius, 
            width = 1
        )

    def update(self, screen: pygame.Surface, dt: float) -> None:
        self.position += self.velocityHat * self.velocity * dt

        self.rect.center = self.position

        screen.blit(self.surface, self.rect)
