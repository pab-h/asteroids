import pygame
import pygame.transform as transform

from pygame import Vector2
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
        self.surface2 = pygame.transform.scale (\
             pygame.image.load("./asteroids/assets/nave3_up.png")\
            .convert_alpha(),(50,50))
        self.surface.set_colorkey((0,0,0))
        self.position = pygame.Vector2(300  ,300)
        self.rect = self.surface.get_rect(center = self.position)
        self.angle = 0
        self.surface_copy = pygame.transform.rotate(self.surface,self.angle)
        self.velocity = pygame.Vector2(0 , 50)
      
           
    def movement(self, screen) -> None:
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]: 
            #self.velocity = self.velocity.rotate(5)
            #self.angularVelocityHat += 5
            #print(self.velocity[1])
            self.velocity = self.velocity.rotate(+5)
            self.angle = self.angle - 5
            self.surface_copy = pygame.transform.rotate(self.surface2,self.angle)
        else:
            self.surface_copy = pygame.transform.rotate(self.surface,self.angle)

        if keys[pygame.K_LEFT]: 
            self.velocity = self.velocity.rotate(-5)
            self.angle = self.angle + 5
            self.surface_copy = pygame.transform.rotate(self.surface2,self.angle)
        else:
            self.surface_copy = pygame.transform.rotate(self.surface,self.angle)
        
        if keys[pygame.K_UP]: 
            self.velocity[1] = self.velocity[1] +2
            self.surface_copy = pygame.transform.rotate(self.surface2,self.angle)
        else:
            if self.velocity[1] > 1:
                self.velocity[1] = self.velocity[1] -3
                self.surface_copy = pygame.transform.rotate(self.surface,self.angle)
            
        
        if keys[pygame.K_SPACE]: 
            #shot = Shot()
            bullet = Bullet(self.rect.x,self.rect.y)
            self.bullet_group.add(bullet)
            
            print("tiro")
            
    def update(self, screen: pygame.Surface, dt: float) -> None:
        
        self.position -= self.velocity * dt
        self.rect.center = self.position
        self.movement(screen)
        
        screen.blit(self.surface_copy,(self.position[0] - int(self.surface_copy.get_width()/2), self.position[1] - int(self.surface_copy.get_height()/2)))
        #screen.blit(self.surface_copy,self.rect)              
        