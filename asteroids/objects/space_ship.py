import pygame

from pygame.sprite import Sprite
from asteroids.interfaces.updateable import Updateable


class Space_Ship (Sprite, Updateable):
    def _init_(self) -> None:
        super().__init__()
        Updateable.__init__(self)
        
        
        self.ship = pygame.image.load('./space_ship.png').convert_alpha()
        self.ship_rect = self.get_rect
        self.ship_position = pygame.Vector2(300,300)
        
       
        
    def update(self, screen: pygame.Surface) -> None:
        self.ship_position += pygame.Vector2(10,10)
        self.ship_rect.center = self.ship_position
        
        screen.blit(self.ship, self.ship_rect)