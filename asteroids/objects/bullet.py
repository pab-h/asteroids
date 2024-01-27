import pygame

from pygame.sprite import Sprite
from asteroids.interfaces.updateable import Updateable


class Bullet(Sprite, Updateable):
    def __init__(self, pos_x,pos_y):
        super().__init__()
        Updateable.__init__(self)
        
        self.image = pygame.Surface((10,10))
        self.image.fill((255,0,0))
        self.rect = self.image.get_rect(center = (pos_x,pos_y))
        
    def update(self, screen: pygame.Surface):
        self.rect.x +=5