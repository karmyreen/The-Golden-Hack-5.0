from typing import Any
import pygame
from random import *


class Germs(pygame.sprite.Sprite):
    def __init__(self, type):
        super().__init__()

        red_frame_1 = pygame.image.load("visuals/red germs/red_germ_0.png").convert_alpha()
        red_frame_2 = pygame.image.load("visuals/red germs/red_germ_1.png").convert_alpha()

        yellow_frame_1 = pygame.image.load("visuals/yellow germs/yellow_germ_0.png").convert_alpha()
        yellow_frame_2 = pygame.image.load("visuals/yellow germs/yellow_germ_1.png").convert_alpha()

        if type == "red":
            self.frames = [red_frame_1,red_frame_2]
            self.speed = 10
         
        if type == "yellow":
            self.frames = [yellow_frame_1,yellow_frame_2]
            self.speed = 6
        
        self.frame_index = 0

        self.image = self.frames[self.frame_index]
        self.rect = self.image.get_rect(center = (choice([84,250,417]),randint(-120,-20)))

    def curr_frame(self):
        self.frame_index += 0.20
        if self.frame_index >= len(self.frames):
            self.frame_index = 0
        self.image = self.frames[int(self.frame_index)]
    
    def update(self):
        self.curr_frame()
        self.rect.y += self.speed
        if self.rect.y > 860:
            self.kill()
            
        return

