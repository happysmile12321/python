import pygame,sys
pygame.init()

Vinfo = pygame.display.Info()
#border = (width,height) = Vinfo.current_w,Vinfo.current_h
border = (width,height) = 800,600
screen = pygame.display.set_mode(border)
cat = pygame.image.load("res/xiaobai.png")
speed=[1,1]
BLACK=0,0,0
catrect = cat.get_rect()


# Feature
## title and icon setting
pygame.display.set_caption('我的游戏')
title = pygame.display.get_caption()
icon = pygame.image.load('./res/flowers/flower.png')
pygame.display.set_icon(icon)


fps = 3000
fclock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                sys.exit()
        elif event.type == pygame.VIDEORESIZE:
            size = width,height = event.size[0],event[1]
            screen = pygame.display.set_mode(size,pygame.RESIZABLE)
    catrect = catrect.move(speed[0],speed[1])
    if catrect.left < 0 or catrect.right > width:
            speed[0]=-speed[0]
    if catrect.top < 0 or catrect.bottom > height:
        speed[1]=-speed[1]
    screen.fill(BLACK)
    screen.blit(cat,catrect)
    fclock.tick(fps) 
    pygame.display.update()



