from settings import *
import pygame
import random

from main import *



bg = pygame.image.load("visuals/scary mouth.png").convert_alpha()
germs = pygame.image.load("visuals/germs.png").conver_alpha()

#pos = [(94,382), (202,383), (313, 287),(400,385),(80,256), (180,480), ( 280,485),(370,487),(430,443)]

pos1 = (94,382)
pos2 = (313, 287)
pos3 = (180,480)







def brushingTeeth():
    
    
    screen.blit(bg, (0,0))

    
    rect = germs.get_rect(center = pos1)
    rec2 = germs.get_rect(center = pos2)
    rec3 = germs.get_rect(center = pos3)

    if(event.type == pygame.MOUSEMOTION):
        x, y = event.pos
        
        if( (pos1-40 <= x <= pos1) and ( pos1+40 <= y <= pos1 )):
            pos1 = -100
        if( (pos2-40 <= x <= pos2) and ( pos2+40 <= y <= pos2 )):
            pos2 = -100
        if( (pos3-40 <= x <= pos3) and ( pos3+40 <= y <= pos3 )):
            pos3 = -100
       

        


   

    


    
