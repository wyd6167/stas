from ui.main import Ui_MainWindow
from PyQt5 import QtWidgets
from ui.login import Ui_login_ui
from PyQt5 import QtWidgets
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import QMouseEvent
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtWidgets import QFrame, QMessageBox, QTableWidgetItem, QApplication, QHeaderView

class MyPyQT_Form(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MyPyQT_Form, self).__init__()
        self.setupUi(self)
        # self.setWindowFlag(Qt.FramelessWindowHint)
    # def mousePressEvent(self, e: QMouseEvent):
    #     if e.button() == Qt.LeftButton:
    #         self._isTracking = True
    #         self._startPos = QPoint(e.x(), e.y())
    #
    # def mouseMoveEvent(self, e: QMouseEvent):  # 重写移动事件
    #     self._endPos = e.pos() - self._startPos
    #     self.move(self.pos() + self._endPos)
    #
    # def mouseReleaseEvent(self, e: QMouseEvent):
    #     if e.button() == Qt.LeftButton:
    #         self._isTracking = False
    #         self._startPos = None
    #         self._endPos = None
if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    A1 = MyPyQT_Form()
    A1.show()
    sys.exit(app.exec_())