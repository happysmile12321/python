# Import static link libraryfile
import pygame,sys
# Init some basic setup,screen
pygame.init()
screen = pygame.display.set_mode((800,600))
# Capture things,and reflush it
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        pygame.display.update()
