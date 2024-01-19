import pygame

from pygame.sprite import Sprite
from asteroids.interfaces.updateable import Updateable

class SpaceShip(Sprite, Updateable):
    def __init__(self) -> None:
        super().__init__()
        Updateable.__init__(self)
        
        self.surface = pygame.image.load("./asteroids/assets/space_ship.png")\
            .convert_alpha()
        self.rect = self.surface.get_rect()
        self.position = pygame.Vector2(300,300)
        self.velocity = pygame.Vector2(50, 50)
        
    def update(self, screen: pygame.Surface, dt: float) -> None:
        self.position += self.velocity * dt
        self.rect.center = self.position
        
        screen.blit(self.surface, self.rect)