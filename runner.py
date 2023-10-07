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

        self.image = self.frames[self.frame_index]
        self.pos = (250,750)
        self.rect = self.image.get_rect(center = self.pos)
        self.key_pressed = False

    def curr_frame(self):
        self.frame_index += 0.25
        if self.frame_index >= len(self.frames):
            self.frame_index = 0
        self.image = self.frames[int(self.frame_index)]
        self.rect = self.image.get_rect(center = self.pos)

    def input(self):
        keys = pygame.key.get_pressed()

        if not self.key_pressed:
            if keys[pygame.K_a] or keys[pygame.K_LEFT]:
                if self.pos == (250,750):
                    self.pos = (84,750)

                elif self.pos == (84,750):
                    self.pos = (84,750)
                
                elif self.pos == (417,750):
                    self.pos = (250,750)
            
                self.key_pressed = True

            elif keys[pygame.K_d] or keys[pygame.K_RIGHT]:
                if self.pos == (250,750):
                    self.pos = (417,750)

                elif self.pos == (417,750):
                    self.pos = (417,750)
                
                elif self.pos == (84,750):
                    self.pos = (250,750)

                self.key_pressed = True

        
    def update(self):
        self.input()
        self.curr_frame()