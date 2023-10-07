import pygame
from random import randint

def rotate_flip(img):
    img = pygame.transform.rotozoom(img,0,2)
    img = pygame.transform.flip(img,True,False)
    return img

class Runner(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        frame1 = pygame.image.load("visuals\\mario run\\mariorun1.png").convert_alpha()
        frame1 = rotate_flip(frame1)

        frame2 = pygame.image.load("visuals\\mario run\\mariorun2.png").convert_alpha()
        frame2 = rotate_flip(frame2)

        frame3 = pygame.image.load("visuals\\mario run\\mariorun3.png").convert_alpha()
        frame3 = rotate_flip(frame3)

        frame4 = 