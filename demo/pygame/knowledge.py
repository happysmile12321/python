import pygame,sys
print('SDL是管理计算机外设的一个库')
print('pygame基于SDL进行封装')
print('pygame经典的2D游戏')
print('pygame也是一款游戏开发引擎，具有参考价值')
# pygame的最小开发框架
## 引入pygame和sys
## 初始化init及设置
## 循环--获取事件并响应，刷新屏幕

# 引入初始化
# 响应事件

pygame.init()
pygame.display.set_mode((200,300))
pygame.display.set_caption("pygame")


# pygame维护1个事件队列。
# pygame.event.get()从pygame事件中拉去事件，并删除,这就是pygame的处理事件。
# pygame.display.update()是用来刷新窗口。
