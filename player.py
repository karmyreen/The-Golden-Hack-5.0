import pygame
from pygame.sprite import _Group
from settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self,groups):
        super().__init__(groups)

        self.image = pygame.image.load("visuals/test.png").convert_alpha()
        self.rect = self.image.get_rect(topleft = (0,0))

        