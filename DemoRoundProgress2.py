import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QApplication, QWidget,QLabel
from PyQt5 import *


# ---第2步---定义圆形进度条类的定义---
class CirBar(QWidget):
    # ---第2-1步---初始化定义---
    def __init__(self):
        super(CirBar, self).__init__()
        # 去边框，去掉边框也就是会去掉右上角退出的“×”，好看，但是强制退出要报错，小bug，可以继续优化
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)  # 设置窗口背景透明

        self.persent = 0
        self.my_thread = MyThread()
        self.my_thread.my_signal.connect(self.GenUpdate)
        self.my_thread.start()
        # 定义更新

    def GenUpdate(self, p):
        self.persent = p
        # 定义绘画事件

    def paintEvent(self, event):
        # 360°分成100等分
        rotateAngle = 360 * self.persent / 100
        # 绘制准备工作，启用反锯齿
        painter = QPainter(self)
        # 启用反锯齿，如果本行注释，那么圆的外线有锯齿，不光滑。
        painter.setRenderHints(QtGui.QPainter.Antialiasing)

        # 外圆底色是blue，注意100,100和内圆的96和96，说明外圆不是正圆，稍大一点，有露出外圆底色一点弧形蓝色
        painter.setBrush(QBrush(QColor("blue")))
        # 250和250是圆点的坐标
        painter.drawEllipse(250, 250, 100, 100)  # 画外圆

        # 内圆底色是黄色
        painter.setBrush(QBrush(QColor("yellow")))
        # 250和250是圆点的坐标
        painter.drawEllipse(250, 250, 96, 96)  # 画内圆
        # 角度渐变(QConicalGradient)
        gradient = QConicalGradient(50, 50, 91)
        # 进度条的画笔颜色
        gradient.setColorAt(1, QColor("red"))
        self.pen = QPen()
        self.pen.setBrush(gradient)  # 设置画刷渐变效果
        self.pen.setWidth(8)
        self.pen.setCapStyle(Qt.RoundCap)
        painter.setPen(self.pen)
        # 250和250是圆点的坐标
        painter.drawArc(QtCore.QRectF(250, 250, 98, 98), int((90 - 0) * 16), -int(rotateAngle * 16))  # 画圆环

        # 中间画笔的颜色，显示动态百分数的颜色
        painter.setPen(QColor("green"))
        # 画中间动态百分比的文字设置和250和250是圆点的坐标
        painter.drawText(QtCore.QRectF(250, 250, 98, 98), Qt.AlignCenter, "%d%%" % self.persent)  # 显示进度条当前进度
        self.update()
#---第3步---创建线程
class MyThread(QThread):
    my_signal = pyqtSignal(int)
    p = 0
    #初始化线程
    def __init__(self):
        super(MyThread, self).__init__()
    #运行线程
    def run(self):
        while True:
            if self.p < 100:
                self.p += 1
                self.my_signal.emit(self.p)
                self.msleep(100)


# ---第4步---
if __name__ == '__main__':
    app = QApplication(sys.argv)

    CirBar = CirBar()
    CirBar.show()
    sys.exit(app.exec_())