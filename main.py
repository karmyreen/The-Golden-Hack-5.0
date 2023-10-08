import pygame, sys
from loader import *
from runner import Runner
from enemies import Germs
from random import randint, choice
from quiz import *

WIDTH, HEIGHT, FPS = read_settings()

pygame.init()

screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Hygiene Hero")
clock = pygame.time.Clock()
game_state = "running"
#defining the background
def import_assets():
    global background
    background = pygame.image.load("visuals/background.png").convert_alpha()
    
import_assets()

runner = pygame.sprite.GroupSingle()
runner.add(Runner())

germs_monsters = pygame.sprite.Group()

timer = pygame.USEREVENT + 1
pygame.time.set_timer(timer,900)

scroll = 0

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

        if pygame.sprite.spritecollide(runner.sprite,germs_monsters,False):
            game_state = "quiz"

            


    if game_state == "quiz":
        screen.fill((0,0,255))

    pygame.display.flip()
    pygame.display.update()
    clock.tick(60)