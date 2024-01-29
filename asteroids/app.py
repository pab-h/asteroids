import pygame

from asteroids.objects.spaceship import SpaceShip
from asteroids.objects.bullet import Bullet


class App:
    pygame.display.set_caption("Asteroid City")
    def __init__(self) -> None:
        self.screen = pygame.display.set_mode(
            size = (600, 600)
        )
        self.clock = pygame.time.Clock()
        self.runnig = False
        self.fps = 60

    def __enter__(self):
        pygame.init()

        return self
    
    def __exit__(self, exc_type, exc_value, traceback) -> None:
        pygame.quit()

    def run(self) -> None:
        dt = 0

        ship = SpaceShip()
        #ship.bullet_group.draw(self.screen)
        bullet = Bullet(ship.position.x,ship.position.y)
        bullet.bullet_group.draw(self.screen)
        self.runnig = True

        while self.runnig:
            self.screen.fill("black")

            ship.update(self.screen, dt)
            bullet.bullet_group.update(self.screen)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.runnig = False
#
#                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
#                    print("Hello World!")
#                    
#                    ship.surface = pygame.transform.scale (\
#             pygame.image.load("./asteroids/assets/nave.png")\
#            .convert_alpha(),(50,50))
                    
            dt = self.clock.tick(self.fps) / 1000