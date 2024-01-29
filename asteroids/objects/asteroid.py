import pygame.draw as draw

import pygame.transform as transform

from pygame.sprite import Sprite

from pygame import Vector2
from pygame import Surface
from pygame import Rect
from pygame import SRCALPHA

from asteroids.interfaces.updateable import Updateable
from asteroids.interfaces.placeable import Placeable

from math import atan2

from random import random
from random import choice

class Asteroid(Sprite, Placeable, Updateable): 
    def __init__(self, position: Vector2) -> None:
        super().__init__()
        Placeable.__init__(self)
        Updateable.__init__(self)

        self.position = position

        self.radius = 50
        self.surface = Surface(
            size = Vector2(2, 2) * self.radius,
            flags = SRCALPHA
        )
        self.rect = self.surface.get_rect()

        self.velocity = 100
        self.velocityHat = Vector2(0, 0)

        self.angle = 0
        self.angularVelocity = (300 - 50) * random() + 50
        self.angularVelocityHat = choice([1, -1])

        self.padding = Vector2(50, 50)

        self.amoutPoints = int((10 - 6) * random()) + 6
        self.points: list[Vector2] = []
        self.centerPoint = Vector2(0, 0)

        self.populatePoints()
        self.setCenterPoint()
        self.sortPoints()
        self.draw()

    def populatePoints(self) -> None:
        deltaTheta = 360 / self.amoutPoints
        deltaThetaMin = 0

        center = Vector2(1, 1) * self.radius

        for i in range(self.amoutPoints):
            deltaThetaMin = i * deltaTheta
            theta = random() * deltaTheta + deltaThetaMin

            polarPoint = Vector2(self.radius, theta)
            point = Vector2.from_polar(polarPoint)
            point = point + center

            self.points.append(point)

    def setCenterPoint(self) -> None:
        start = Vector2(0, 0)

        self.centerPoint = sum(self.points, start) / len(self.points)

    def sortPoints(self) -> None: 
        def angle(point: Vector2) -> float:
            v = point - self.centerPoint

            return atan2(v.y, v.x)
        
        self.points.sort(key = angle)

    def collidePoint(self, point: Vector2) -> bool: 
        distance = self.position.distance_to(point)

        return distance - self.radius <= 0
    
    def collideRect(self, rect: Rect) -> bool: 
        distance = rect.center - self.position
        distanceHat = Vector2(0, 0)

        if distance.length() > 0:
            distanceHat = distance.normalize()

        collidePoint = self.position + self.radius * distanceHat

        return rect.collidepoint(collidePoint)
    
    def draw(self) -> None:
        draw.polygon(
            surface = self.surface, 
            color = "red", 
            points = self.points, 
            width = 3
        )

    def update(self, screen: Surface, dt: float) -> None:
        self.position += self.velocityHat * self.velocity * dt
        self.angle += self.angularVelocity * self.angularVelocityHat * dt

        rotatedSurface = transform.rotate(self.surface, self.angle)

        self.rect.center = self.position

        self.rect.center -= Vector2(rotatedSurface.get_size()) / 2

        screen.blit(rotatedSurface, self.rect.center)