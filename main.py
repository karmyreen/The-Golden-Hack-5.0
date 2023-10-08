import pygame, sys
from loader import *
from runner import Runner

WIDTH, HEIGHT, FPS = read_settings()

pygame.init()

screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Hygiene Hero")
clock = pygame.time.Clock()

#defining the background
def import_assets():
    global background
    background = pygame.image.load("visuals/background.png").convert_alpha()
    
import_assets()

runner = pygame.sprite.GroupSingle()
runner.add(Runner())

scroll = 0

while True:
    screen.blit(background,(0,0))    

    for event in pygame.event.get():
        keys = pygame.key.get_pressed()
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    for i in range(0,3):
        screen.blit(background,(0,i * -835 + scroll))

    scroll += 10
    if scroll > 835:
        scroll = 0

    runner.draw(screen)
    runner.update()

    pygame.display.flip()
    pygame.display.update()
    clock.tick(60)