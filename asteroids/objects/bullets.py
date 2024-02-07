from pygame import Surface

from asteroids.interfaces.updateable import Updateable
from asteroids.objects.bullet import Bullet

from typing import Iterator

class Bullets(Updateable):
    def __init__(self) -> None:
        super().__init__()

        self.bullets: list[Bullet] = []

    def __iter__(self) -> Iterator[Bullet]:
        return iter(self.bullets)

    def addAll(self, bullets: list[Bullet]) -> None:
        self.bullets = self.bullets + bullets

    def kill(self, bullet: Bullet) -> None:
        self.bullets.remove(bullet)

    def update(self, screen: Surface, dt: float) -> None:
        for bullet in self.bullets:
            bullet.update(screen, dt)