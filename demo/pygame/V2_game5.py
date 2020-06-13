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
        if event.type == pygame.MOUSEMOTION:
            pos = event.pos
            rel = event.rel
            print('MOUSE is moving')
            print('我当前的座标',pos)
            print('上次的座标',rel)
            if event.buttons[0]==1:
                print('鼠标左键被按下了')
            else:
                print('鼠标左键没有被按下')
            if event.buttons[1]==1:
                print('鼠标中键被按下了')
            else:
                print('鼠标中键没有被按下')
            if event.buttons[2]==1:
                print('鼠标右键被按下了')
            else:
                print('鼠标右键没有被按下')

        elif event.type == pygame.MOUSEBUTTONUP:
            print('MOUSE UP')
            if event.button == 3:
                print('鼠标右键被释放了')
            elif event.button == 1:
                print('鼠标左键被释放了')
            elif event.button == 2:
                print('鼠标中键被释放了')
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print('MOUSE DOWS')
            if event.button == 1:
                print('鼠标左键[Pressed]')
            elif event.button == 2:
                print('鼠标中键[Pressed]')
            elif event.button == 3:
                print('鼠标右键[Pressed]')

        pygame.display.update()
