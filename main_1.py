import pygame, sys
from loader import *


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

while True:

    screen.blit(background,(0,0))

    for event in pygame.event.get():
        keys = pygame.key.get_pressed()
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    clock.tick(60)