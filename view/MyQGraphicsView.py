from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QGraphicsView, QGraphicsScene, QGraphicsPixmapItem, QLabel, QWidget
from PyQt5.QtWidgets import QWidget, QApplication, QLabel
from PyQt5.QtCore import QRect, Qt
from PyQt5 import QtCore
from PyQt5.QtGui import QImage, QPixmap, QPainter, QPen
import cv2
import sys
from PyQt5.QtWidgets import QGraphicsView, QGraphicsRectItem
from ui.drawrect import InteractiveGraphicsRectItem
from PyQt5 import  QtWidgets,QtGui


class MyGraphicsView(QGraphicsView):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.label = None
        self.mousePressed = False
        self.showresult = None
        self.flag = 0

        self.setMouseTracking(True)

    def setLabel(self, label):
        self.label = label

    def setPar(self, showresult):
        self.showresult = showresult

    def setFlag(self, flag):
        self.flag = flag
    # 鼠标点击事件
    def mousePressEvent(self, event):

        if self.flag == 0:
            #拖动
            self.showresult.mousePressEvent(event)
        elif self.flag == 1:
            #绘制矩形框
            self.label.mousePressEvent(event)
        else:
            #拖动 拉伸 删除
            super().mousePressEvent(event)
            if event.buttons() == QtCore.Qt.RightButton:
                pos = event.pos()
                scene_pos = self.mapToScene(pos)
                items = self.scene().items(scene_pos)
                print(items)
                if isinstance(items[0], InteractiveGraphicsRectItem):
                    self.scene().removeItem(items[0])
    # 鼠标释放事件
    def mouseReleaseEvent(self, event):

        if self.flag == 0:
            self.showresult.mouseReleaseEvent(event)
        elif self.flag == 1:
            self.label.mouseReleaseEvent(event)
        else:
            super().mouseReleaseEvent(event)

    # 鼠标移动事件
    def mouseMoveEvent(self, event):
        if self.flag == 0:
            self.showresult.mouseMoveEvent(event)
        elif self.flag == 1:
            self.label.mouseMoveEvent(event)
        else:
            super().mouseMoveEvent(event)

    # 绘制事件
    def paintEvent(self, event):
        super().paintEvent(event)
        if self.flag!=0:
            self.label.paintEvent(event)

    @QtCore.pyqtSlot()
    def zoomIn(self):
        self.zoom(MyGraphicsView.factor)

    @QtCore.pyqtSlot()
    def zoomOut(self):
        self.zoom(1 / MyGraphicsView.factor)

    def zoom(self, f):
        self.scale(f, f)
        if self.scene() is not None:
            self.centerOn(self.scene().image_item)
if __name__ == '__main__':
    app = QApplication([])
    widget = QWidget()
    scene = QGraphicsScene()
    pixmap = QPixmap('image.jpg')
    item = QGraphicsPixmapItem(pixmap)
    scene.addItem(item)

    view = MyGraphicsView(widget)
    view.setScene(scene)

    label = QLabel()
    label.setPixmap(pixmap)
    label.setAlignment(Qt.AlignCenter)

    widget.setLayout(view)

    widget.show()
    app.exec_()
