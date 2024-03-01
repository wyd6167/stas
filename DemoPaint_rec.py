from PyQt5.QtWidgets import QWidget, QApplication, QLabel
from PyQt5.QtCore import QRect, Qt, QRectF
from PyQt5.QtGui import QImage, QPixmap, QPainter, QPen
import cv2
import sys
from ui.drawrect import InteractiveGraphicsRectItem
from PyQt5 import QtCore


class MyLabel(QLabel):
    x0 = 0
    y0 = 0
    x1 = 0
    y1 = 0
    flag = False
    view = None
    scene = None
    showres = None
    def setView(self, view):
        self.view = view

    def setScene(self, scene):
        self.scene = scene

    def setPar(self, showRes):
        self.showres = showRes
    # 鼠标点击事件
    def mousePressEvent(self, event):
        if event.buttons() == QtCore.Qt.LeftButton:
            self.flag = True
            self.x0 = event.x()
            self.y0 = event.y()

        # elif event.buttons() == QtCore.Qt.RightButton:
        #     items = self.scene.items(event.scenePos())
        #     print(items)
        #     self.scene.removeItem(items[0])


    # 鼠标释放事件
    def mouseReleaseEvent(self, event):
        self.flag = False

        x0 = min(self.x0, self.x1)
        y0 = min(self.y0, self.y1)
        x1 = max(self.x0, self.x1)
        y1 = max(self.y0, self.y1)
        width = x1 - x0
        height = y1 - y0

        # 矩形
        rect = QRectF(x0, y0, width, height)
        rect_item = InteractiveGraphicsRectItem(rect, 5)
        self.scene.addItem(rect_item)
        self.showres.rectangle.append([x0, y0, width, height])

        # self.view.show()

    # 鼠标移动事件
    def mouseMoveEvent(self, event):
        if self.flag:
            self.x1 = event.x()
            self.y1 = event.y()
            self.update()

    # 绘制事件
    def paintEvent(self, event):
        super().paintEvent(event)
        # rect =QRect(self.x0, self.y0, abs(self.x1-self.x0), abs(self.y1-self.y0))
        # 这里换成任意方向的矩形框
        # 标注框的左上角和右下角坐标
        x0 = min(self.x0, self.x1)
        y0 = min(self.y0, self.y1)
        x1 = max(self.x0, self.x1)
        y1 = max(self.y0, self.y1)
        width = x1 - x0
        height = y1 - y0

        # 矩形
        rect = QRect(x0, y0, width, height)
        painter = QPainter(self)
        painter.setPen(QPen(Qt.red, 2, Qt.SolidLine))
        # painter.drawRect(rect)
        # painter.eraseRect(rect)
        painter.end()






class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.resize(675, 500)
        self.move(100, 50)
        self.setWindowTitle('在label中绘制矩形')
        self.lb = MyLabel(self)  # 重定义的label
        # 这里直接读取图片
        img = QPixmap(r'F:\python\mypy1\stas_system\stas_system\utils\algorithm\res.png')
        # 往显示视频的Label里 显示QImage
        self.lb.setPixmap(img)
        self.lb.setCursor(Qt.CrossCursor)  # 图片可以绘制
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    x = Example()
    sys.exit(app.exec_())
