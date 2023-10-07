import pygame
from settings import *

class Level():
    def __init__(self):

        self.display = pygame.display.get_surface()
        self.visible = pygame.sprite.Group()
        self.obstacles = pygame.sprite.Group()

    def run(self):
        pass