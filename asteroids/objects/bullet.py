from typing import Any
import pygame

from pygame.sprite import Sprite
from asteroids.interfaces.updateable import Updateable


class Bullet(Sprite, Updateable):
    def __init__(self) -> None:
        super().__init__()
        Updateable.__init__(self)
        
        self.surface = pygame.transform.scale (\
             pygame.image.load("./asteroids/assets/bullet.png")\
            .convert_alpha(),(15,15))
        self.position = pygame.Vector2(0,0)
        self.rect = self.surface.get_rect(center = self.position)
        self.velocity = pygame.Vector2(10 , 10)
    
        
        self.bullet_group = pygame.sprite.Group()
    
    def bullet_shot(self, screen, x, y):
        self.position[0] = x
        self.position[1] = y
        
        screen.blit((self.surface,self.rect))
    
    def update(self, screen: pygame.Surface, dt: float) -> None:
        self.rect.x += self.velocity *dt
        #screen.blit(self.surface,self.rect)              