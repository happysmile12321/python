import pygame,sys
pygame.init()
Vinfo = pygame.display.Info()
border = (width,height) = Vinfo.current_w,Vinfo.current_h
screen = pygame.display.set_mode(border)
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
disinfo = pygame.display.Info()
print(disinfo)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
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
    pygame.display.update()



