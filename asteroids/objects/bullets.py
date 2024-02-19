import pygame.display as display

from pygame import Surface
from pygame import Vector2

from asteroids.interfaces.updateable import Updateable
from asteroids.objects.bullet import Bullet

from typing import Iterator

class Bullets(Updateable):
    def __init__(self) -> None:
        super().__init__()

        self.bullets: list[Bullet] = []
        self.center = self.getScreenCenter()
        self.cutRadius = self.center.length()

    def __iter__(self) -> Iterator[Bullet]:
        return iter(self.bullets)

    def addAll(self, bullets: list[Bullet]) -> None:
        self.bullets = self.bullets + bullets

    def kill(self, bullet: Bullet) -> None:
        self.bullets.remove(bullet)

    def getScreenCenter(self) -> Vector2:
        size = display.get_window_size()

        return Vector2(size) / 2

    def garbage(self) -> None:
        for bullet in self.bullets:
            radiusVector = self.center - bullet.position
            radius = radiusVector.length()
            
            if radius > self.cutRadius:
                self.kill(bullet)

    def update(self, screen: Surface, dt: float) -> None:
        self.garbage()

        for bullet in self.bullets:
            bullet.update(screen, dt)