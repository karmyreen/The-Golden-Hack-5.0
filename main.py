import pygame, sys
from loader import *

WIDTH, HEIGHT, FPS = read_settings()
class Game():
    def __init__(self):
        
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('Hygiene Hero')
        self.clock = pygame.time.Clock()
    

    def run(self):

        while True:

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                
                    pygame.quit()
                    sys.exit()

            pygame.display.update()
            self.clock.tick(FPS)


if __name__ == '__main__':
	game = Game()
	game.run()
    













