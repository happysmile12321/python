import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import requests
import threading
import os
import zipfile
from PIL import Image


class Workchange(QThread):
    """docstring for WorkThread"""
    change_done = pyqtSignal()

    def __init__(self):
        super(Workchange, self).__init__()

    def run(self):
        url = self.url
        name = url.split('/')[-1] + '.zip'
        print('正在下载资源',name)
        data = requests.get(url).content
        with open(name,'wb') as f:
            f.write(data)
        print('下载完成！')

        path = os.environ['HOME']+'/shimeji/'
        if not os.path.exists(path):
            os.makedirs(path)
        print('正在解压资源...')
        z = zipfile.ZipFile(name, 'r')
        z.extractall(path=path)
        z.close()

        for i in range(1,47):
            os.rename(path + 'shime%s.png'% str(i),path+str(i)+'.png')
            pri_image = Image.open(path+'%s.png' %str(i))
            pri_image.transpose(Image.FLIP_LEFT_RIGHT).save(path+'-%s.png'%str(i))

        for i in os.listdir(path):
            os.system('convert %s %s'%(path+i,path+i))
        print('解压完成')
        os.remove(name)
        self.change_done.emit()

class Workinit(QThread):
    """docstring for WorkThread"""
    init_done = pyqtSignal(dict)

    def __init__(self):
        super(Workinit, self).__init__()

    def run(self):
        for i in range(3,90):
            threading.Thread(target=self.load,args=(i,)).start()

    def load(self,i):
            url = ''' http://pepeswap.com/thumb/%s''' %str(i)
            data  = requests.get(url).content
            name = str(i)
            dict_data = dict(data=data,name=name)
            self.init_done.emit(dict_data)

class DQListWidget(QListWidget):
    def __init__(self):
        super(DQListWidget, self).__init__()
        self.workinit = Workinit()
        self.workchange = Workchange()
        self.workchange.change_done.connect(self.change_done)
        self.workinit.init_done.connect(self.load_picture)
        self.workinit.start()
        self.itemDoubleClicked.connect(self.change)

    def change_done(self):
        QMessageBox.about(self,'提示','更换完成！(*>﹏<*)')

    def change(self,item):
        self.workchange.url = 'http://pepeswap.com/mascot/' + item.text()
        self.workchange.start()

    def load_picture(self,dict_data):        
        item = QListWidgetItem(dict_data['name'])
        item.setSizeHint(QSize(10, 128))
        self.addItem(item)
        pixmap = QPixmap()
        label = QLabel()
        pixmap.loadFromData(dict_data['data'])
        label.setPixmap(pixmap)
        self.setItemWidget(item,label)

class Mywin(QWidget):
    def __init__(self):
        super(Mywin, self).__init__()
        list_ = DQListWidget() 
        layout = QVBoxLayout(self)
        layout.addWidget(list_) 
        self.setLayout(layout) 


app = QApplication(sys.argv)
mywin = Mywin() # 实例化一个窗口小部件
mywin.setWindowTitle('Hello world!') # 设置窗口标题
mywin.show() #显示窗口
sys.exit(app.exec())

