import pygame,sys
pygame.init()
screen = pygame.display.set_mode((800,600))

# Feature 
# keyboard Event

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.unicode != "":
                print('$',event.key,event.mod)
            # if press Q,quit
            if (event.key == pygame.K_q) & (event.mod == 1):
                sys.exit()
        pygame.display.update()
