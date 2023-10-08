import pygame, sys
from loader import *
from runner import Runner
from enemies import Germs
from random import randint, choice
#from quiz import random_toothbrush_tip, random_laundry_tip, random_handwashing_tip, random_false_toothbrush_tip, random_false_laundry_tip, random_false_handwashing_tip
#from quiz import ai_stuff
from ai import generate_ai

WIDTH, HEIGHT, FPS = read_settings()


pygame.init()

FONT_SIZE = 24
font = pygame.font.SysFont(None, FONT_SIZE)

screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Hygiene Hero")
clock = pygame.time.Clock()
game_state = "title"  
curr_time = 0
#defining the background
def import_assets():
    global title_screen
    global background
    background = pygame.image.load("visuals/background.png").convert_alpha()
    title_screen = pygame.image.load("visuals/hygienehero_title.png").convert_alpha()
    

def display_score():
    global curr_time
    curr_time = int((pygame.time.get_ticks()/100) - start_time) 
    score_display = font.render(f"score {curr_time}",False,(0,0,0))
    score_rect = score_display.get_rect(topleft = (20,50))
    screen.blit(score_display,score_rect)

import_assets()
start_time = 0

runner = pygame.sprite.GroupSingle()
runner.add(Runner())

germs_monsters = pygame.sprite.Group()

timer = pygame.USEREVENT + 1
pygame.time.set_timer(timer,1100)

scroll = 0



def prompt_question():
    hygiene_type_li = ["toothbrush","handwashing","laundry"]
    hygiene_type = choice(hygiene_type_li)
    if hygiene_type == "toothbrush":
        if randint(0,1):   #true question
            question, _,_ = generate_ai("You are a video game character giving tips on how to brush your teeth effectively.", "Give the user 3 short tips in point form on how to brush their teeth effectively. Each tip should only be 10-15 words long. Don't include backslash n for new lines in the answer.")
            answer = True
        else:
            question, _,_ = generate_ai("You are a video game character giving obviously false tips on how to brush their teeth effectively.", "Give the user 3 short obviously false tips in point form on how to brush their teeth more effectively. Each tip should only be 10-15 words long. Don't include backslash n for new lines in the answer.")
            answer = False

    elif hygiene_type == "handwashing":
        if randint(0,1):
            question, _,_ = generate_ai("You are a video game character giving tips on how to wash hands effectively.", "Give the user 3 short tips in point form on how to wash hands effectively. Each tip should only be 10-15 words long. Don't include backslash n for new lines in the answer.")
            answer = True
        else:
            question, _,_ = generate_ai("You are a video game character giving obviously false tips on how to wash hands effectively.", "Give the user 3 short obviously false tips in point form on how to wash hands more effectively. Each tip should only be 10-15 words long. Don't include backslash n for new lines in the answer.")
            answer = False

    elif hygiene_type == "laundry":
        if randint(0,1):
            question, _,_ = generate_ai("You are a video game character giving tips on how to do laundry effectively.", "Give the user 3 short tips in point form on how to do their laundry more effectively. Each tip should only be 10-15 words long. Don't include backslash n for new lines in the answer.")
            answer = True
        else:
            question, _,_ = generate_ai("You are a video game character giving obviously false tips on how to do laundry effectively.", "Give the user 3 short obviously false tips in point form on how to do their laundry more effectively. Each tip should only be 10-15 words long. Don't include backslash n for new lines in the answer.")
            answer = False
    
    return question, answer

question, answer = prompt_question()

while True:
    screen.blit(background,(0,0))

    for event in pygame.event.get():
        keys = pygame.key.get_pressed()
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if game_state == "running":
            if event.type == timer:
                germs_monsters.add(Germs(choice(["yellow","yellow","red"])))
        
        if game_state == "title":
            if keys[pygame.K_SPACE]:
                game_state = "running"
                germs_monsters.empty()

    if game_state == "running":
        for i in range(0,3):
            screen.blit(background,(0,i * -835 + scroll))

        scroll += 10
        if scroll > 835:
            scroll = 0

        runner.draw(screen)
        runner.update() 

        germs_monsters.draw(screen)
        germs_monsters.update()

        display_score()
        
        print(curr_time)

        if pygame.sprite.spritecollide(runner.sprite,germs_monsters,False):
            game_state = "quiz"

            
    if game_state == "title":
        
        screen.blit(title_screen,(0,0))
        
        #tooth,laundry,hand_washing = ai_stuff()

    if game_state == "quiz":
        #screen.fill((0,0,255))
        # Define the font and font size to use for the variable
        
        true = pygame.image.load("visuals/image_50.png").convert_alpha()
        false = pygame.image.load("visuals/image2_350x114.png").convert_alpha()


        # Define the position of the true button
        true_position = (250, 750)
        false_position = (250, 620)
        # Get the rectangle of the true button image
        true_rect = true.get_rect(center=true_position)
        false_rect = false.get_rect(center=false_position)
        # Render the example variable as a Pygame surface
        surface = font.render(question, True, (0, 0, 0), (255, 255, 255))

        # Blit the example surface and the true button image onto the screen

        screen.blit(surface, (0, 250))
        screen.blit(true, true_rect) #350x128
        screen.blit(false, false_rect) #350x114

        mx,my = pygame.mouse.get_pos()
        
        click = pygame.mouse.get_pressed()
        if (mx >= 75 and mx<=425) and ( my>=686 and my <=814):
            if click[0]:
                user_answer = True
                print(user_answer)

                if user_answer == answer:
                    game_state = "title"
                    question, answer = prompt_question()
                    germs_monsters.empty()
                    game_state = "title"
                    germs_monsters.empty()
                    game_state = "running"
                    
                    
                else:
                    germs_monsters.empty()
                    game_state = "title"
                    curr_time = int((pygame.time.get_ticks()/100))
                    question, answer = prompt_question()
                    germs_monsters.empty()

        if (mx >= 75 and mx<=425) and (my >= 556 and my <=680):
            if click[0]:
                user_answer = False
        
                print(user_answer)

                if user_answer == answer:
                    game_state = "title"
                    question, answer = prompt_question()
                    germs_monsters.empty()
                    game_state = "title"
                    germs_monsters.empty()
                    game_state = "running"

                else:
                    germs_monsters.empty()
                    game_state = "title"
                    curr_time = int((pygame.time.get_ticks()/100))
                    question, answer = prompt_question()
                    germs_monsters.empty()
        # Define the example variable
        

        # Render the example variable as a Pygame surface
        surface = font.render(question, True, (0, 0, 0),(255,255,255))

        # Blit the example surface onto the screen
        screen.blit(surface, (0, 250
                              ))
        

    pygame.display.flip()
    pygame.display.update()
    clock.tick(60)