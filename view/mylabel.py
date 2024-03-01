from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import QImage, QPixmap
import cv2
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys


class MyLabel(QLabel):
    def __init__(self, text):
        super(MyLabel, self).__init__()
        # self.label = QLabel(self)

    # def paintEvent(self, event):
    #     super().paintEvent(event)
    #     # rect =QRect(self.x0, self.y0, abs(self.x1-self.x0), abs(self.y1-self.y0))
    #     # 这里换成任意方向的矩形框
    #     # 标注框的左上角和右下角坐标
    #     # x0 = min(self.x0, self.x1)
    #     # y0 = min(self.y0, self.y1)
    #     # x1 = max(self.x0, self.x1)
    #     # y1 = max(self.y0, self.y1)
    #     # width = x1 - x0
    #     # height = y1 - y0
    #
    #     # 矩形
    #     rect = QRect(0, 0, 1000, 1000)
    #     painter = QPainter(self)
    #     painter.begin(self.qScrollArea)
    #     painter.setPen(QPen(Qt.red, 2, Qt.SolidLine))
    #     painter.drawRect(rect)
    #     painter.end()
    def mousePressEvent(self, e: QMouseEvent):
        if e.buttons() == QtCore.Qt.LeftButton:
            self.flag = True

    def mouseReleaseEvent(self, e: QMouseEvent):  # 鼠标释放事件重写
        self.flag = False
        self.movex = ""
        self.movey = ""

    def mouseMoveEvent(self, e: QMouseEvent):
        tmph = self.qScrollArea.horizontalScrollBar()
        tmpv = self.qScrollArea.verticalScrollBar()
        if self.flag:
            self.x1 = e.x()
            self.y1 = e.y()
        if self.movex != "" and self.movey != "":
            self.label_x = self.label_x + (self.x1 - self.movex)
            self.label_y = self.label_y + (self.y1 - self.movey)
            # tmph.setValue(tmph.value()+self.x1 - self.movex)
            # tmpv.setValue(tmpv.value()+self.y1 - self.movey)
            tmph.setValue(tmph.value() + self.movex - self.x1)
            tmpv.setValue(tmpv.value() + self.movey - self.y1)
        self.movex = self.x1
        self.movey = self.y1

    def wheelEvent(self, e):
        self.angle = e.angleDelta() / 8
        self.angleY = self.angle.y()
        if self.angleY > 0:
            if self.resize_point >= 1 and self.resize_point <= 19:  # 此处的self.resize_point初始值为10，作为缩放系数
                self.resize_point += 1
        elif self.angleY < 0:
            if self.resize_point >= 2 and self.resize_point <= 20:
                self.resize_point -= 1
        x_1 = e.x()
        y_1 = e.y()
        x2 = (x_1 - self.label.x()) / self.label.width()  # 第一次鼠标坐标x比值
        y2 = (y_1 - self.label.y()) / self.label.height()  # 第一次鼠标坐标y比值
        x2_ = x_1 - self.label.x()
        y2_ = y_1 - self.label.y()
        # 由于cV2包得到图像并非是我们所需的图片对象，这里先是对图片宽高根据缩放系数进行改变，然后将图片转换为QImage对象，在转换为QPixmap对象
        self.cur_resimg = cv2.resize(self.cur_img, (
            (int(self.cur_img.shape[1] * self.resize_point / 10)),
            (int(self.cur_img.shape[0] * self.resize_point / 10))))
        img2 = cv2.cvtColor(self.cur_resimg, cv2.COLOR_BGR2RGB)  # 转RGB格式，以在Qlabel中显示
        QImage = QtGui.QImage(img2, self.cur_resimg.shape[1], self.cur_resimg.shape[0], 3 * self.cur_resimg.shape[1],
                              QtGui.QImage.Format_RGB888)
        self.pixmap = QtGui.QPixmap((QImage).scaled(self.cur_resimg.shape[1], self.cur_resimg.shape[0]))

        self.label_w = self.cur_resimg.shape[1]
        self.label_h = self.cur_resimg.shape[0]
        if int(x2) == 0 and int(y2) == 0:
            x3 = x2
            y3 = y2
            Lmx2 = x3 * self.label_w
            Lmy2 = y3 * self.label_h
            self.label_x = int(x_1 - Lmx2)
            self.label_y = int(y_1 - Lmy2)
            self.groupBox.resize(self.label_w, self.label_h)
            # self.label.setGeometry(QtCore.QRect(self.label_x, self.label_y, self.label_w, self.label_h))
            # self.label.setGeometry(QtCore.QRect(0, 0, self.label_w, self.label_h))
            self.label.resize(self.label_w, self.label_h)
            self.label.setPixmap(self.pixmap)
            tmph = self.qScrollArea.horizontalScrollBar()
            tmpv = self.qScrollArea.verticalScrollBar()
            # tmph.setValue(tmph.value()-self.label_x)
            # tmpv.setValue(tmpv.value()-self.label_y)
            tmph.setValue(tmph.value() + Lmx2 - x_1)
            tmpv.setValue(tmpv.value() + Lmy2 - y_1)

    def paintEngine(self):
        rect = QRect(0, 0, 1000, 1000)
        painter = QPainter(self.label1)
        painter.begin(self)
        painter.setPen(QPen(Qt.red, 2, Qt.SolidLine))
        painter.drawRect(rect)
        painter.end()
