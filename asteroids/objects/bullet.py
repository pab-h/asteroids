from typing import Any
import pygame

from pygame.sprite import Sprite
from asteroids.interfaces.updateable import Updateable


class Bullet(Sprite, Updateable, x, y):
    def __init__(self, *groups) -> None:
        super().__init__(*groups)
        #Updateable.__init__(self)
        
        self.surface = pygame.transform.scale (\
             pygame.image.load("./asteroids/assets/shot.png")\
            .convert_alpha(),(15,15))
        self.position = pygame.Vector2(x,y)
        self.rect = self.surface.get_rect(center = self.position)
        self.velocity = pygame.Vector2(10 , 10)
    
        
        self.bullet_group = pygame.sprite.Group()
    
    def update(self, screen: pygame.Surface, dt: float) -> None:
        self.rect.x += self.velocity *dt
        #screen.blit(self.surface,self.rect)              