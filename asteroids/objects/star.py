from pygame import Surface
from pygame import SRCALPHA
from pygame import Vector2
from pygame import Color

import pygame.draw as draw

from pygame.sprite import Sprite

from math import sin
from math import pi

from random import choice

from asteroids.interfaces.placeable import Placeable
from asteroids.interfaces.updateable import Updateable

class Star(Sprite, Placeable, Updateable):
    def __init__(self, position: Vector2) -> None:
        super().__init__()
        Placeable.__init__(self)
        Updateable.__init__(self)

        self.position = position
        self.radius = 1
        self.range = .5
        self.color = Color(choice([ "#ffffff", "#ffec9c", "#ba0045", "#3b00c5", "#0882cf" ]))
        self.velocity = choice([ 1, 3, 6 ])
        self.phase = choice([ 0, (1/2) * pi, pi, (3/2) * pi, 2 * pi ])

        self.time = 0

        self.surface = Surface(
            size = Vector2(2, 2) * self.radius,
            flags = SRCALPHA
        )
        self.rect = self.surface.get_rect()

        draw.circle(self.surface, self.color, self.rect.center, self.radius)

    def update(self, screen: Surface, dt: float) -> None:
        self.time = self.time + dt

        self.rect.center = self.position + self.range * Vector2(
            sin(self.velocity * self.time + self.phase), 
            - sin(self.velocity * self.time + self.phase) ** 2
        )

        screen.blit(self.surface, self.rect)
