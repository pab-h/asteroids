import pygame, sys

from asteroids.objects.spaceship import SpaceShip
from asteroids.objects.stars import Stars
from asteroids.objects.asteroids import Asteroids
from asteroids.objects.hud import HUD
from asteroids.objects.bullets import Bullets
from asteroids.interfaces.button import Button


class App:
    def __init__(self) -> None:
        pygame.display.set_caption("Asteroids")

        self.screen = pygame.display.set_mode(
            size = (600, 600)
        )
        self.clock = pygame.time.Clock()
        self.runnig = False
        self.fps = 60

        self.spaceShip = SpaceShip()
        self.stars = Stars()
        self.asteroids = Asteroids(self.spaceShip)
        self.bullets = Bullets()
        self.hud = None


        self.BG = pygame.image.load("asteroids/assets/bk3.png")
        self.title = pygame.image.load("asteroids/assets/Title.png")
        
        #self.sound_Play = pygame.mixer.Sound("asteroids/assets/extraShip.mp3")
        #self.sound_Play = pygame.mixer.music.load("asteroids/assets/extraShip.mp3")
        
    def __enter__(self):
        pygame.init()
        
        self.sound_Play = pygame.mixer.music.load("asteroids/assets/music_intro2.mp3")
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.2)
        
        self.sound_Play = pygame.mixer.Sound("asteroids/assets/extraShip.mp3")
        self.explosion = pygame.mixer.Sound("asteroids/assets/explosion2.mp3")
        self.zap = pygame.mixer.Sound("asteroids/assets/zap.mp3")
        self.hud = HUD()

        return self
    
    def __exit__(self, exc_type, exc_value, traceback) -> None:
        pygame.quit()
        
    def get_font(self,size):
        return pygame.font.Font("asteroids/assets/Minecraft.ttf", size)
        
    def run(self) -> None:
        dt = 0

        self.stars.populate(300)
        self.asteroids.populate(10)

        self.runnig = True

        while self.runnig:
            self.screen.fill("black")

            for bullet in self.bullets:
                asteroid = self.asteroids.collidePoint(bullet.position) 

                if asteroid:
                    self.hud.score +=1
                    self.explosion.play()
                    self.hud.update(self.screen, dt)
                    fragments = asteroid.rupture()
                    self.asteroids.addAll(fragments)
                    self.asteroids.kill(asteroid)
                    self.bullets.kill(bullet)

            asteroid = self.asteroids.collideRect(self.spaceShip.rect)

            if asteroid:
                print("TOME UM DANO PARA LARGAR DE SER BESTA")
                self.hud.lifes -= 1
            self.stars.update(self.screen, dt)
            self.asteroids.update(self.screen, dt)
            self.spaceShip.update(self.screen, dt)
            self.bullets.update(self.screen, dt)
            self.hud.update(self.screen, dt)

            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.runnig = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.zap.play()
                        bullet = self.spaceShip.shoot()
                        self.bullets.addAll([ bullet ])
                    
            dt = self.clock.tick(self.fps) / 1000
            
    def start_screen(self) -> None:
        
        while True:
            self.screen.blit(self.BG, (0, 0))
            self.screen.blit(self.title, (50 , 20))

            MENU_MOUSE_POS = pygame.mouse.get_pos()

            #MENU_TEXT = self.get_font(100).render("MAIN MENU", True, "#b68f40")
            #MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

            PLAY_BUTTON = Button(image=pygame.image.load("asteroids/assets/Play_button_3.png").convert_alpha(), pos=(150, 450), 
                                text_input="Play", font=self.get_font(60), base_color="#d7fcd4", hovering_color="White")
            SCORE_BUTTON = Button(image=pygame.image.load("asteroids/assets/Play_button_3.png"), pos=(450, 450), 
                                text_input="Score", font=self.get_font(55), base_color="#d7fcd4", hovering_color="White")

            #self.screen.blit(MENU_TEXT, MENU_RECT)

            #for button in [PLAY_BUTTON, OPTIONS_BUTTON, SCORE_BUTTON]:
            for button in [PLAY_BUTTON, SCORE_BUTTON]:
                button.changeColor(MENU_MOUSE_POS)
                button.update(self.screen)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                        self.sound_Play.play()
                        pygame.mixer.music.stop()
                        
                        self.sound_Play = pygame.mixer.music.load("asteroids/assets/game_bk.mp3")
                        pygame.mixer.music.play(-1)
                        pygame.mixer.music.set_volume(0.2)
        
                        self.run()
                        pygame.quit()
                        sys.exit()
                    if SCORE_BUTTON.checkForInput(MENU_MOUSE_POS):
                        pygame.quit()
                        sys.exit()

            pygame.display.update()

    
