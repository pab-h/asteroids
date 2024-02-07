from pygame import Surface

from asteroids.interfaces.updateable import Updateable
from asteroids.objects.bullet import Bullet

class Bullets(Updateable):
    def __init__(self) -> None:
        super().__init__()

        self.bullets: list[Bullet] = []

    def addAll(self, bullets: list[Bullet]) -> None:
        self.bullets = self.bullets + bullets

    def update(self, screen: Surface, dt: float) -> None:
        for bullet in self.bullets:
            bullet.update(screen, dt)