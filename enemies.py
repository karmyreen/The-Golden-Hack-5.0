import pygame
from random import randint

from pygame.sprite import _Group

class Germs(pygame.sprite.Sprite):
    def __init__(self, *groups: _Group) -> None:
        super().__init__(*groups)