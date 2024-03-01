import sys

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import win32ui
import win32api,win32con

from demo7.ui_demo7 import Ui_frmMain

class MyMainWindow(QMainWindow, Ui_frmMain):
    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)
        self.setupUi(self)
        self.setFixedSize(1200, 680) #固定大小
        self.okButton.clicked.connect(self.ok_action)  # 点击登录按钮
        #self.setWindowFlags(Qt.FramelessWindowHint)  # 无边框
        self.startAnimation()
        self.initQSS()

    def login_by_phone_action(self):
        '''
        点击 手机登录 按钮
        '''
        self.pushButtonPhone.setStyleSheet('color:#0088ff;')
        self.pushButtonAcount.setStyleSheet('color:black;')

    def login_by_acount_action(self):
        '''
        点击 帐号登录 按钮
        '''
        self.pushButtonAcount.setStyleSheet('color:#0088ff;')
        self.pushButtonPhone.setStyleSheet('color:black;')

    def adj_login(self, user, pwd):
        '''
        验证登录是否正确
        '''
        return True

    def ok_action(self):
        '''
        点击确定按钮事件
        '''
        user = self.lineEditUser.text().strip()
        pwd = self.lineEditPwd.text().strip()
        if user == '' or pwd == '':
            win32api.MessageBox(0, "用户名或密码不能为空,请重新输入!", "登录提醒", win32con.MB_ICONWARNING)
            return False

        if self.adj_login(user, pwd) == False:
            win32api.MessageBox(0, "用户名或密码不正确,请重新输入!", "登录提醒", win32con.MB_ICONWARNING)
            return False

        self.close()

    def cancel_action(self):
        '''
        点击"取消"按钮事件
        '''
        self.close()

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
            #print(style_sheet)
            self.setStyleSheet(style_sheet)

if __name__=="__main__":
    app = QApplication(sys.argv)
    myWin = MyMainWindow()
    myWin.show()
    sys.exit(app.exec_())
