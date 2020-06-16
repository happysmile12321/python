import pygame,sys
pygame.init()
border = (width,height) = 800,600
screen = pygame.display.set_mode(border,flags=pygame.RESIZABLE)
# pygame support jpg,png,gif ... 
cat = pygame.image.load("res/xiaobai.png")
speed=[1,1]
BLACK=0,0,0
# 任何导入pygame的图像都会被解析为surface对象
# surface.get_rect()用于形成一个与对象外切的矩形对象。
catrect = cat.get_rect()
# 矩形对象可以有

# (x,y)    --------
#          |      |
#          |      |
#          --------  (x,y)

fps = 120
fclock = pygame.time.Clock()
#控制帧速度，即窗口刷新速度：
#clock.tick(100)表示每秒钟100次刷新帧
#tick 滴答声
#clock.tick(framerate)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        # 发生了键盘的敲击事件
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                sys.exit()
#            elif event.key == pygame.K_DOWN:
#            elif event.key == pygame.K_LEFT:
#            elif event.key == pygame.K_RIGHT:
            

        # 矩形移动
        # catrect.move(speed[0],speed[1])
        # (0,0)------>x
        #     |
        #     |
        #     |
        #     |
        #     |
        #     ↓
        #     y
        #　沿x移动speed[0]个像素
        #　沿y移动speed[1]个像素
    catrect = catrect.move(speed[0],speed[1])
        # 如果矩形的左上角座标(catrect.left)小于0，也就是说它移动到了上面的外面。那么应该将上下方向的移动进行反向。


    if catrect.left < 0 or catrect.right > width:
            speed[0]=-speed[0]
    if catrect.top < 0 or catrect.bottom > height:
        speed[1]=-speed[1]
    # 填充RGB颜色作为背景，否则会形成残影，而且必须先填充背景，然后再由blit进行渲染图片到矩形
    screen.fill(BLACK)
    # 将1个图像绘制在另外1个图像上，src图像，dest图像
    # 作用是让图像跟着矩形的移动而移动
    screen.blit(cat,catrect)
    fclock.tick(fps) 
    pygame.display.update()



