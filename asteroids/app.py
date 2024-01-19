import pygame

from asteroids.objects.space_ship import Space_Ship

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

        ship = Space_Ship()
        
        self.runnig = True

        while self.runnig:
            # Atualize aqui

            # Desenhe aqui
            
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.runnig = False

            dt = self.clock.tick(self.fps) / 1000