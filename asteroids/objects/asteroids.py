from pygame import Vector2
from pygame import Surface
from pygame import display
from pygame import Rect

from pygame.sprite import Group

from asteroids.interfaces.updateable import Updateable
from asteroids.interfaces.placeable import Placeable

from asteroids.objects.asteroid import Asteroid

from random import random

from typing import Optional

class Asteroids(Group, Updateable):
    def __init__(self, target: Placeable) -> None:
        super().__init__()
        Updateable.__init__(self)

        self.target = target
        self.radius = self.getSpawnRadius()
        self.center = self.getSpawnCenter()
        self.asteroids: list[Asteroid] = []
        
    def getSpawnCenter(self) -> Vector2:
        size = display.get_window_size()

        return Vector2(size) / 2

    def getDirection(self, asteroid: Asteroid) -> Vector2:
        distance = self.target.position - asteroid.position 

        return distance.normalize()

    def populate(self, amout: int) -> None:
        for _ in range(amout):
            asteroid = self.createAsteroid()
            self.asteroids.append(asteroid)

    def createAsteroid(self) -> Asteroid:
        spawnPolarPoint = Vector2(self.radius, random() * 360)
        spawnPoint = Vector2.from_polar(spawnPolarPoint)
        spawnPoint += self.center

        asteroid = Asteroid(spawnPoint)
        asteroid.velocityHat = self.getDirection(asteroid)

        return asteroid

    def getSpawnRadius(self) -> float:
        width = display.get_window_size()[0]
        offsetRadius = 10
        
        return offsetRadius + width / 2 ** 0.5
    
    def rebound(self) -> None:
        for asteroid in self.asteroids:
            distance = asteroid.position - self.center
            distance = distance.length()

            if distance - self.radius > 0:
                asteroid.velocityHat.rotate_ip(180)

    def collidePoint(self, point: Vector2) -> Optional[Asteroid]:
        for asteroid in self.asteroids:
            if asteroid.collidePoint(point):
                return asteroid
        return None
    
    def collideRect(self, rect: Rect) -> Optional[Asteroid]:
        for asteroid in self.asteroids:
            if asteroid.collideRect(rect):
                return asteroid
        return None

    def update(self, screen: Surface, dt: float) -> None:
        self.rebound()

        for asteroid in self.asteroids:
            asteroid.update(screen, dt)
