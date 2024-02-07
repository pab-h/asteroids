import pygame.image as image
import pygame.transform as transform

from pygame import Surface
from pygame import Vector2

from pygame.sprite import Sprite

from asteroids.interfaces.placeable import Placeable
from asteroids.interfaces.updateable import Updateable

class Bullet(Sprite, Placeable, Updateable):
    def __init__(self, shooter: Placeable, direction: Vector2) -> None:
        super().__init__()
        Placeable.__init__(self)
        Updateable.__init__(self)
    
        self.position = shooter.position.copy()
        self.direction = direction.copy()
        self.velocity = 300

        self.surface = image\
            .load("./asteroids/assets/bullet.png")\
            .convert_alpha()
        self.rect = self.surface.get_rect()

        self.align()

    def align(self) -> None:
        directionAngle = self.direction.as_polar()[1]

        self.surface = transform.rotate(self.surface, -(directionAngle + 90))

    def update(self, screen: Surface, dt: float) -> None:
        self.position += self.velocity * self.direction * dt

        self.rect.center = self.position

        screen.blit(self.surface, self.rect)