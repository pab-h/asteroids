from pygame import Surface
from pygame import Vector2
from pygame import K_w
from pygame import K_d
from pygame import K_a
from pygame import K_UP
from pygame import K_LEFT
from pygame import K_RIGHT

from pygame.sprite import Sprite

import pygame.image as image
import pygame.key as key
import pygame.transform as transform

from asteroids.interfaces.placeable import Placeable
from asteroids.interfaces.updateable import Updateable

from asteroids.objects.bullet import Bullet

class SpaceShip(Sprite, Placeable, Updateable):
    def __init__(self) -> None:
        super().__init__()
        Placeable.__init__(self)
        Updateable.__init__(self)

        self.position = Vector2(300, 300)

        self.surface = image\
            .load("./asteroids/assets/nave.png")\
            .convert_alpha()
        self.rect = self.surface.get_rect()

        self.direction = Vector2(self.rect.centerx, self.rect.y) - self.position
        self.direction.normalize_ip()

        self.acceleration = 100
        self.velocityHat = self.direction.copy()
        self.velocity = 100
        self.angularVelocity = 250
        self.friction = 25

    def shoot(self) -> Bullet:
        return Bullet(self, self.direction)

    def move(self, dt: float) -> None:
        keys = key.get_pressed()

        if keys[K_w] or keys[K_UP]:
            self.velocityHat = self.direction.copy()
            self.velocity += self.acceleration * dt

        if keys[K_d] or keys[K_RIGHT]:
            self.direction.rotate_ip(self.angularVelocity * dt)

        if keys[K_a] or keys[K_LEFT]:
            self.direction.rotate_ip(-self.angularVelocity * dt)

        self.velocity -= self.friction * dt
        self.velocity = max(0, self.velocity)
        self.velocity = min(200, self.velocity)

        self.position += self.velocity * self.velocityHat * dt

    def update(self, screen: Surface, dt: float) -> None:
        self.move(dt)

        directionAngle = self.direction.as_polar()[1]

        rotatedSurface = transform.rotate(self.surface, -(directionAngle + 90))
        rotatedRect = rotatedSurface.get_rect()

        self.rect.center = self.position
        rotatedRect.center = self.position

        screen.blit(rotatedSurface, rotatedRect)