import pygame, math

from pygame.sprite import Sprite
from asteroids.interfaces.updateable import Updateable
from asteroids.objects.bullet import Bullet


class SpaceShip(Sprite, Updateable):
    def __init__(self) -> None:
        super().__init__()
        Updateable.__init__(self)
        
        self.surface = pygame.transform.scale (\
             pygame.image.load("./asteroids/assets/nave3.png")\
            .convert_alpha(),(50,50))
        self.w, self.h = self.surface.get_size()
        self.position = pygame.Vector2(300,300)
        self.rect = self.surface.get_rect(center = self.position)
        #self.angle = pygame.Vector2(0,0)
        self.velocity = pygame.Vector2(10 , 10)
        
        self.bullet_group = pygame.sprite.Group()
    
        
    
    def rotate(self):
        """Rotate the image of the sprite around its center."""
        # `rotozoom` usually looks nicer than `rotate`. Pygame's rotation
        # functions return new images and don't modify the originals.
        self.image = pygame.transform.rotozoom(self.surface, 5, 1)
        # Create a new rect with the center of the old rect.
        self.rect = self.image.get_rect(center=self.rect.center)
    

    
    def creat_bullet(self):
        return Bullet(self.position.x, self.position.y)
        
            
    def movement(self, screen) -> None:
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]: 
            #self.rect = self.blitRotate(screen, self.surface, self.position , (self.w/2, self.h/2),5)
            self.velocity = self.velocity.rotate(5)
            
            print(self.velocity[0])
            
        if keys[pygame.K_LEFT]: 
            self.velocity = self.velocity.rotate(-5)
        
        if keys[pygame.K_UP]: 
            self.velocity[1] = self.velocity[1] + 1       
        
        if keys[pygame.K_SPACE]: 
            #shot = Shot()
            self.bullet_group.add(self.creat_bullet())
            
            print("tiro")
            
    def update(self, screen: pygame.Surface, dt: float) -> None:
        self.position -= self.velocity * dt
        self.rect.center = self.position
       
        self.movement(screen)
        #self.rotate()
        #self.rect = self.blitRotate(screen, self.surface, self.position , (self.w/2, self.h/2),5)
        
        screen.blit(self.surface,self.rect)              
        
      