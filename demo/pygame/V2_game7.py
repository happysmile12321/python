import pygame,sys
pygame.init()
screen = pygame.display.set_mode((800,600))
# Feature
# 自定义事件
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        pygame.display.update()
