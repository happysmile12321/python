import pygame,sys
# pygame事件处理机制

# 基本概念
# 键盘事件
# 鼠标事件
# 改造小球例子

#　基本概念

# 对游戏，事件很重要
# 事件队列--缓存所有pygame接受到的事件
# 用事件处理程序，如一取出
# 原则上先到先处理
# pygame.event.EventType--1个封装的类--只有属性--没有方法--pojo--可以通过它获得事件参数
# 用户可以编写程序写自己的事件类型

## | 说明     | EventType       | Attribute |
## |----------|-----------------|-----------|
## | 系统     | QUIT            | 退出      |
## | 系统     | ACTIVEEVENT     | 激活      |
## | 键盘     | KEYDOWN         | 按下      |
## | 键盘     | KEYUP           | 抬起      |
## | 鼠标     | MOUSEMOTION     | 移动      |
## | 鼠标     | MOUSEBUTTONUP   | 按下      |
## | 鼠标     | MOUSEBUTTONDOWN | 抬起      |
## | 游戏杆   | JOYXISMOTION    |           |
## | 游戏杆   | JOYBALLMOTION   |           |
## | 游戏杆   | JOYHATMOTION    |           |
## | 游戏杆   | JOYBUTTONUP     |           |
## | 游戏杆   | JOYBUTTONDOWN   |           |
## | 窗口     | VIDEORESIZE     |           |
## | 窗口     | VIDEOEXPOSE     |           |
## | 用户定义 | USEREVENT       | 代码      |

if event.type == pygame.KEYDOWN:
    elif event.key == pygame.K_LEFT: #键的名称
    elif event.unicode # 键的unicode吗
    elif event.mod # 键的按键模式 

#　处理事件

pygame.event.get()


#只获取1个单一事件，然后将事件删除
#如果没有事件，则返回<no-event>
pygame.event.poll()

#默认删除所有事件
pygame.event.clear()

pygame事件队列仅能存储128个队列



#　操作事件队列

pygame.event.set_blocked(type or typelist)

# 测试某个事件类型是否被禁止，如果被禁止，则返回true
# 否则，返回false
pygame.event.get_blocked(type)

pygame.event.set_allowed(type or typelist)

#　生成事件

# 获得1个用户定义的事件
pygame.event.post(Event)

# 创建1个给定类型的事件
pygame.event.Event(type,dict) #类型，属性


#　键盘事件

## | 键盘     | KEYDOWN         | 按下      |
unicode 按键的unicode吗 --与操作系统的平台相关--有时不会返回--实际不建议使用
key 按键的常量名
```
K_a
K_b
...
K_z
```
# 没有K_Q的存在。如果要判断的化，需要结合MOD键--mode--修饰键


按键的修饰符--除了所按的键之外，按键提供的修饰键的状态
eg：

KMOD_NONE
KMOD_LSHIFT
KMOD_RSHIFT
KMOD_SHIFT
KMOD_CAPS
KMOD_LCTRL
KMOD_RCTRL
KMOD_CTRL
KMOD_LALT
KMOD_RALT
KMOD_ALT
KMOD_LMETA
KMOD_RMETA
KMOD_META
KMOD_NUM
KMOD_MODE

mod 按键修师符的组合值
event.mod---> 修饰符的或运算的组合值
event.mod = KMOD_ALT | KMOD_SHIFT

## | 键盘     | KEYUP           | 抬起      |



#  鼠标事件

## | 鼠标     | MOUSEMOTION     | 移动      |

event.pos 鼠标当前的座标值(x,y),相对与pygame软件窗口左上角
event.rel 鼠标相对运动距离(x,y),相对于上次事件
event.buttons 鼠标的按键状态(a,b,c) 对应于鼠标的2个键-左，中，右如果处于按下时为1，否则为0
这个特性可以用来画画嘛。

        if event.type == pygame.MOUSEMOTION:
            print('MOUSE is moving')
        elif event.type == pygame.MOUSEBUTTONUP:
            print('MOUSE UP')
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print('MOUSE DOWS')
## | 鼠标     | MOUSEBUTTONUP   | 按下      |
event.pos 鼠标当前的座标值(x,y),相对与pygame软件窗口左上角
event.button 鼠标按下键编号n , 取值0/1/2,分别对应三个键 

鼠标左键为1，右键为3

            if event.button == 1:
                print('鼠标左键[Pressed]')
            elif event.button == 2:
                print('鼠标中键[Pressed]')
            elif event.button == 3:
                print('鼠标右键[Pressed]')

有的鼠标还带滑轮，那么滚动滑轮可能返回任意值。
任意值与设备本身的驱动和硬件有关。



## | 鼠标     | MOUSEBUTTONDOWN | 抬起      |

同上


#  改造小球例子



