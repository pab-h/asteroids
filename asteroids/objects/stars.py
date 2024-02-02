from pygame import Surface
from pygame import Vector2

import pygame.display as display

from pygame.sprite import Group

from asteroids.interfaces.updateable import Updateable

from asteroids.objects.star import Star

from random import random

class Stars(Group, Updateable):
    def __init__(self) -> None:
        super().__init__()
        Updateable.__init__(self)

        self.stars: list[Star] = []

    def populate(self, n: int) -> None:
        for _ in range(n):
            position = display.get_window_size()[0] * Vector2(random(), random())

            star = Star(position)

            self.stars.append(star)

    def update(self, screen: Surface, dt: float) -> None:
        for star in self.stars:
            star.update(screen, dt)
