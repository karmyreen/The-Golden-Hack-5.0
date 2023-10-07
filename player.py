import pygame
from pygame.sprite import _Group
from settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self,groups):
        super().__init__(groups)