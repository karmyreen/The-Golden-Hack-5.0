from settings import *
import pygame
import random

from main import *



bg = pygame.image.load("visuals/scary mouth.png").convert_alpha()
germs = pygame.image.load("visuals/germs.png").conver_alpha()

pos = [(94,382), (202,383), (313, 287),(400,385),(80,256), (180,480), ( 280,485),(370,487),(430,443)]

pos1 = (94,382)
pos2 = (313, 287)
pos3 = (180,480)







def brushingTeeth():
    
    
    screen.blit(bg, (0,0))

    
    rect = germs.get_rect(center = pos1)
    rec2 = germs.get_rect(center = pos2)
    rec3 = ger

   

    


    
