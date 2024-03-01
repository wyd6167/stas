from ui.login import Ui_login_ui
from ui.demo1.ui_demo1 import Ui_frmMain
from PyQt5 import QtWidgets
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import QMouseEvent
from PyQt5.QtCore import *
class MyPyQT_Form(QtWidgets.QMainWindow, Ui_frmMain):
    def __init__(self):
        super(MyPyQT_Form, self).__init__()
        self.setupUi(self)
        # self.show
        # 隐藏原始的框
        self.setWindowFlag(Qt.FramelessWindowHint)
        # self.setAttribute(Qt.WA_TranslucentBackground)
    def mousePressEvent(self, e: QMouseEvent):
        if e.button() == Qt.LeftButton:
            self._isTracking = True
            self._startPos = QPoint(e.x(), e.y())

    def mouseMoveEvent(self, e: QMouseEvent):  # 重写移动事件
        self._endPos = e.pos() - self._startPos
        self.move(self.pos() + self._endPos)

    def mouseReleaseEvent(self, e: QMouseEvent):
        if e.button() == Qt.LeftButton:
            self._isTracking = False
            self._startPos = None
            self._endPos = None

    def closeWindowAnimation(self):
        '''
        关闭时的动画效果
        '''
        self.animation = QPropertyAnimation(self, b"windowOpacity")
        self.animation.setDuration(1000)
        self.animation.setStartValue(1)
        self.animation.setEndValue(0)
        self.animation.start()
        self.animation.finished.connect(self.close)

    def startAnimation(self):
        '''
        启动时的动画效果
        '''

        self.animation = QPropertyAnimation(self, b"windowOpacity")
        self.animation.setDuration(1000)
        self.animation.setStartValue(0)
        self.animation.setEndValue(1)
        self.animation.start()

    def initQSS(self):
        '''
        初始化样式
        '''
        style_file = QFile("style.css")
        if style_file.open(QFile.ReadOnly | QFile.Text):
            stream = QTextStream(style_file)
            style_sheet = stream.readAll()
            # print(style_sheet)
            self.setStyleSheet(style_sheet)