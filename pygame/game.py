import sys
import pygame
class Game:
    def __init__(self):
        pygame.init() 
        HEIGHT: int = 600
        WIDTH = 600 

        self.screen = pygame.display.set_mode((HEIGHT, WIDTH))
        self.clock = pygame.time.Clock()
    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                    
            pygame.display.update()
            self.clock.tick(60)

Game().run()