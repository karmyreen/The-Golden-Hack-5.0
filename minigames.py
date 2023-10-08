from settings import *
import pygame
import random
from ai import generate_ai

from main import *

def selectMinigame():
    minigame_choice = random.randint(1,3)
    if minigame_choice == 1:
        brushingTeeth()
    if minigame_choice == 2:
        doingLaundry()
    if minigame_choice == 3:
        usingDeoderant()

bg = pygame.image.load("visuals/scary mouth.png").convert_alpha()
germs = pygame.image.load("visuals/germs.png").conver_alpha()

#pos = [(94,382), (202,383), (313, 287),(400,385),(80,256), (180,480), ( 280,485),(370,487),(430,443)]

pos1 = (94,382)
pos2 = (313, 287)
pos3 = (180,480)
score = 0 






def brushingTeeth():


    
    
    screen.blit(bg, (0,0))

    
    rect = germs.get_rect(center = pos1)
    rec2 = germs.get_rect(center = pos2)
    rec3 = germs.get_rect(center = pos3)

    while (score != 3 ):


        if(event.type == pygame.MOUSEMOTION):
            x, y = event.pos
            
            if( (pos1-40 <= x <= pos1) and ( pos1+40 <= y <= pos1 )):
                pos1 = -100
                score += 1 
            if( (pos2-40 <= x <= pos2) and ( pos2+40 <= y <= pos2 )):
                pos2 = -100
                score += 1 
            if( (pos3-40 <= x <= pos3) and ( pos3+40 <= y <= pos3 )):
                pos3 = -100
                score += 1 


    #WHEN MINIGAME OVER
    toothbrush_example1, toothbrush_example2, toothbrush_example3 = generate_ai("You are a video game character giving tips on how to brush your teeth effectively.", "Give the user 3 short tips in point form on how to brush their teeth effectively. Each tip should only be 10-15 words long. Don't include backslash n for new lines in the answer.")

    
def doingLaundry():
    ## CODE HERE




    #WHEN MINIGAME OVER
    laundry_example1, laundry_example2, laundry_example3 = generate_ai("You are a video game character giving tips on how to do laundry effectively.", "Give the user 3 short tips in point form on how to do their laundry more effectively. Each tip should only be 10-15 words long. Don't include backslash n for new lines in the answer.")

def usingDeoderant():
    ## CODE HERE


    
    #WHEN MINIGAME OVER
    deoderant_example1, deoderant_example2, deoderant_example3 = generate_ai("You are a video game character giving tips on how to use deoderant effectively.", "Give the user 3 short tips in point form on how to use deoderant effectively. Each tip should only be 10-15 words long. Don't include backslash n for new lines in the answer.")