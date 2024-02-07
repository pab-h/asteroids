import pygame

from asteroids.objects.spaceship import SpaceShip
from asteroids.objects.stars import Stars
from asteroids.objects.asteroids import Asteroids
from asteroids.objects.hud import HUD
from asteroids.objects.bullets import Bullets

class App:
    def __init__(self) -> None:
        pygame.display.set_caption("Asteroids")

        self.screen = pygame.display.set_mode(
            size = (600, 600)
        )
        self.clock = pygame.time.Clock()
        self.runnig = False
        self.fps = 60

        self.spaceShip = SpaceShip()
        self.stars = Stars()
        self.asteroids = Asteroids(self.spaceShip)
        self.bullets = Bullets()
        self.hud = None

    def __enter__(self):
        pygame.init()

        self.hud = HUD()

        return self
    
    def __exit__(self, exc_type, exc_value, traceback) -> None:
        pygame.quit()

    def run(self) -> None:
        dt = 0

        self.stars.populate(300)
        self.asteroids.populate(10)

        self.runnig = True

        while self.runnig:
            self.screen.fill("black")

            for bullet in self.bullets:
                asteroid = self.asteroids.collidePoint(bullet.position) 

                if asteroid:
                    fragments = asteroid.rupture()
                    self.asteroids.addAll(fragments)
                    self.asteroids.kill(asteroid)
                    self.bullets.kill(bullet)

            asteroid = self.asteroids.collideRect(self.spaceShip.rect)

            if asteroid:
                print("TOME UM DANO PARA LARGAR DE SER BESTA")

            self.stars.update(self.screen, dt)
            self.asteroids.update(self.screen, dt)
            self.spaceShip.update(self.screen, dt)
            self.bullets.update(self.screen, dt)
            self.hud.update(self.screen, dt)

            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.runnig = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        bullet = self.spaceShip.shoot()
                        self.bullets.addAll([ bullet ])
                    
            dt = self.clock.tick(self.fps) / 1000