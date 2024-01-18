import pygame

class App:
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

        self.runnig = True

        while self.runnig:
            # Atualize aqui

            # Desenhe aqui

            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.runnig = False

            dt = self.clock.tick(self.fps) / 1000