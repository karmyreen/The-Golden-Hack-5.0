import pygame
from random import randint

def rotate_flip(img):
    img = pygame.transform.rotozoom(img,0,2)
    img = pygame.transform.flip(img,True,False)
    return img

class Runner(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        frame1 = pygame.image.load("visuals/player_animation/player_run_0.png").convert_alpha()
        
        frame2 = pygame.image.load("visuals/player_animation/player_run_1.png").convert_alpha()

        frame3 = pygame.image.load("visuals/player_animation/player_run_2.png").convert_alpha()

        frame4 = pygame.image.load("visuals/player_animation/player_run_3.png").convert_alpha()

        self.frames = [frame1,frame2,frame3,frame4]
        self.frame_index = 0

        self.pos = (250,750)

    def curr_frame(self):
        self.frame_index += 0.25
        if self.frame_index >= len(self.frame_index):
            self.frame_index = 0
        self.image = self.frames[int(self.frame_index)]
        self.rect = self.image.get_rect(center = self.pos)

    def input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a] or keys[pygame._Left]:
            if self.pos == (250,750):
                self.pos = (84,750)

            if self.pos == (84,750):
                self.pos = self.pos
            
            if self.pos == (417,)
        
        