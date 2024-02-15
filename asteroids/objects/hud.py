from pygame import Surface
from pygame import SRCALPHA

from pygame.sprite import Sprite
from pygame.font import Font

from asteroids.interfaces.updateable import Updateable

class HUD(Sprite, Updateable):
    def __init__(self) -> None:
        super().__init__()
        

        self.score = 0
        self.lifes = 3

        self.surface = Surface(
            size = (600, 50),
            flags = SRCALPHA
        )
        self.rect = self.surface.get_rect()

        self.font = Font("asteroids/assets/Minecraft.ttf", 50)

    def update(self, screen: Surface, dt: float) -> None:

        scoreSurface = self.font.render(f"Score: { self.score }", True, "white")
        lifesSurface = self.font.render(f"<3 { self.lifes }", True, "white")

        self.surface.blit(scoreSurface, (10, 10))
        self.surface.blit(lifesSurface, (475, 10))

        screen.blit(self.surface, self.rect)
