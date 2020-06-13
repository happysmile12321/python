import pygame,sys
print('本章将介绍游戏有更多自定义的方法')


# 设置pygame的屏幕相关模式
pygame.display.set_mode(r=(0,0),flag=0)
r-->resolution  width,height
flags:
    # 可调节
    pygame.RESIZABLE
    # 无边框
    pygame.NOFRAME
    # 全屏
    pygame.FULLSCREEN


# 生成屏幕相关的信息
pygame.display.Info()
# 产生一个显示信息的对象VideoInfo，表示当前屏幕的参数信息
# curren_w 当前显示模式或像素的宽度
# curren_h 当前显示模式或像素的高度


# 窗口标题和图标

# 有些操作习题不提供第二个icon的显示，因此有时不设置第2个参数
pygame.display.set_caption(title,icontitle=None) 设置标题

pygame.display.set_icon() 

# 返回当前设置的窗口的标题和小标题内容
# return (title,icontitle)
pygame.display.get_caption()

# 窗口感知和刷新


# 当窗口在系统中显示--屏幕绘制--非图标化
pygame.display.get_active()


pygame.display.flip()


pygame.display.update()

# pygame还可以支持OpenGL 和 硬件加速
# surf https://www.pygame.org




