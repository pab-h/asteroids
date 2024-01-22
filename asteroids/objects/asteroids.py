import pygame

from pygame.sprite import Group

from asteroids.interfaces.updateable import Updateable
from asteroids.interfaces.placeable import Placeable

from asteroids.objects.asteroid import Asteroid

from random import random

class Asteroids(Group, Updateable):
    def __init__(self, target: Placeable) -> None:
        super().__init__()
        Updateable.__init__(self)

        self.target = target
        self.maxAsteroids = 10
        self.radius = self.getSpawnRadius()
        self.center = self.getSpawnCenter()
        self.asteroids = self.populate()

    def getSpawnCenter(self) -> pygame.Vector2:
        size = pygame.display.get_window_size()

        return pygame.Vector2(size) / 2

    def getDirection(self, asteroid: Asteroid) -> pygame.Vector2:
        distance = self.target.position - asteroid.position 

        return distance.normalize()

    def populate(self) -> list[Asteroid]:
        asteroids = []

        for _ in range(self.maxAsteroids):
            asteroid = self.createAsteroid()
            asteroids.append(asteroid)

        return asteroids

    def createAsteroid(self) -> Asteroid:
        spawnPoint = pygame.Vector2(self.radius, random() * 360)
        spawnPoint = pygame.Vector2.from_polar(spawnPoint)
        spawnPoint += self.center

        asteroid = Asteroid(spawnPoint)
        asteroid.velocityHat = self.getDirection(asteroid)

        return asteroid

    def getSpawnRadius(self) -> float:
        width = pygame.display.get_window_size()[0]
        offsetRadius = 10
        
        return offsetRadius + width / 2 ** 0.5
    
    def rebound(self) -> None:
        for asteroid in self.asteroids:
            distance = asteroid.position - self.center
            distance = distance.length()

            if distance - self.radius > 0:
                asteroid.velocityHat.rotate_ip(180)

    def update(self, screen: pygame.Surface, dt: float) -> None:
        self.rebound()

        for asteroid in self.asteroids:
            asteroid.update(screen, dt)