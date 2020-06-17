import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import time
import random
import os


def random_probability(r):
    s = random.randint(1,100)
    if r >= s:
        return True
    else:
        return False

class Donghua(QWidget):
    def __init__(self):
        super(Donghua, self).__init__()
        self.desktop = QApplication.desktop()
        self.screenRect = self.desktop.screenGeometry()
        self.HEIGHT = self.screenRect.height()
        self.WIDTH = self.screenRect.width()
        self.setWindowFlags(Qt.FramelessWindowHint)
        # self.setWindowFlags(Qt.SplashScreen)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.timer = QTimer()
        self.timer.timeout.connect(self.update)
        self.img_timer = QTimer()
        self.img_timer.timeout.connect(self.update_img)
        self.label = QLabel(self)
        self.label.setScaledContents(True)
        layout = QVBoxLayout(self)
        layout.addWidget(self.label)
        self.setLayout(layout)
        self.index = 0
        self.x = 0
        self.is_right = True
        self.m_flag = False
        self.action_dcit = {
        'left_go':(1,3),
        'right_go':(-3,-1),
        'left_hold':(5,7),
        'right_hold':(-7,-5),
        'left_release':(4,4),
        'right_release':(-4,-4),
        'left_down':(18,19),
        'right_down':(-19,-18),
        'left_crawl':(12,14),
        'right_crawl':(-14,-12),
        # 'left_rest':(15,17),
        # 'right_rest':(-17,-15),
        'left_rest':(26,27),
        'right_rest':(-27,-26),
        'left_rest2':(27,29),
        'right_rest2':(-29,-27),
        }
        self.action = 'right_release'
        self.pre_action = ''
        # 控制窗体移动及各种动作切换计时器
        self.timer.start(100)
        # 控制图片切换计时器
        self.img_timer.start(200)

    #监听鼠标动作
    def mousePressEvent(self, event):
        x = (event.globalPos()-self.pos()).x()
        y = (event.globalPos()-self.pos()).y()
        if event.button() == Qt.LeftButton and x < 128 and y < 128:
            self.m_flag = True
            self.m_Position = event.globalPos()-self.pos()  # 获取鼠标相对窗口的位置
            event.accept()

            if self.is_right:
                self.action='right_hold'
            else:
                self.action='left_hold'
            self.setCursor(QCursor(Qt.OpenHandCursor))

    def mouseMoveEvent(self, QMouseEvent):
        if Qt.LeftButton and self.m_flag:
            self.move(QMouseEvent.globalPos()-self.m_Position)  # 更改窗口位置
            QMouseEvent.accept()

    #鼠标左键释放
    def mouseReleaseEvent(self, QMouseEvent):
        self.m_flag = False
        if self.is_right:
            self.action = 'right_release'
        else:
            self.action = 'left_release'

        #手动将其放入屏幕边缘
        if self.x <= 0 and self.y > 0:
            self.action = 'left_crawl'
        elif self.x + self.width >= self.WIDTH and self.y > 0:
            self.action = 'right_crawl'

        self.setCursor(QCursor(Qt.ArrowCursor))

    #动作更新
    def update(self):
        self.width = self.geometry().width()
        self.height = self.geometry().height()
        self.x = self.geometry().x()
        self.y = self.geometry().y()
        # print(self.x,self.y)
        exec('self.%s()'% self.action)


    def right_crawl(self):
        if self.y > 0:
            self.y -= 10
            self.setGeometry(self.x,self.y,100,100)
        else:
            self.action = 'right_release'

    def left_crawl(self):
        if self.y > 0:
            self.y -= 10
            self.setGeometry(self.x,self.y,100,100)
        else:
            self.action = 'left_release'

    def right_down(self):
        if self.index+1 == self.action_dcit[self.action][1]:
            self.action = 'right_go'
    
    def left_down(self):
        if self.index+1 == self.action_dcit[self.action][1]:
            self.action = 'left_go'

    def right_release(self):
        if self.y + self.height > self.HEIGHT:
            self.action = 'right_down'

        else:
            self.action = 'right_release'
            self.y += 100
            self.setGeometry(self.x,self.y,100,100)


    def left_release(self):

        if self.y + self.height > self.HEIGHT:
            self.action = 'left_down'

        else:
            self.action = 'left_release'
            self.y += 100
            self.setGeometry(self.x,self.y,100,100)

    def right_go(self):
        self.x += 5
        self.action = 'right_go'
        if self.x + self.width> self.WIDTH:
            if random_probability(30):
                self.action = 'right_crawl'
            else:
                self.is_right = False
                self.action = 'left_go'

        if random_probability(1):
            self.action = 'right_rest'

        self.setGeometry(self.x,self.y,100,100)



    def left_go(self):
        self.x -= 5
        self.action = 'left_go'
        if self.x < 0:
            if random_probability(30):
                self.action = 'left_crawl'
            else:
                self.is_right = True
                self.action = 'right_go'

        if random_probability(1):
            self.action = 'left_rest'

        self.setGeometry(self.x,self.y,100,100)

    def right_rest(self):
        if random_probability(1):
            self.action = 'right_go'

    def left_rest(self):
        if random_probability(1):
            self.action = 'left_go'

    def right_hold(self):
        pass

    def left_hold(self):
        pass

    #更新图片
    def update_img(self):
        start_index,end_index = self.action_dcit[self.action]
        if self.pre_action != self.action:
            self.index = start_index
            self.pre_action = self.action

        if self.index == end_index:
            self.index = start_index
        else:
            self.index += 1
        q = QPixmap(path +'%s.png' % self.index)
        self.label.setPixmap(q)
        

if __name__ == '__main__':
    path = os.environ['HOME']+'/shimeji/'
    app = QApplication(sys.argv)
    mywin = Donghua()
    mywin.show()
    sys.exit(app.exec())


