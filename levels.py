import pygame
from settings import *

class Level():
    def __init__(self):

        self.display = pygame.display.get_surface()
        # self.visible = pygame.sprite.Group()
        # self.obstacles = pygame.sprite.Group()

        self.background = pygame.image.load("visuals/background.png").convert_alpha()
        self.background_rect = self.background.get_rect(topleft = (0,0))


    def run(self):
        self.display.blit(self.background,self.background_rect)