import sys

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import win32ui
import win32api,win32con

from demo2.UI_login import *
from demo2.UI_reg import Ui_regedit


'''
登录对话框
'''
class loginDialog(QtWidgets.QDialog, Ui_login):
    def __init__(self):
        super(loginDialog, self).__init__()
        self.setupUi(self)
        self.label.setPixmap(QPixmap.fromImage(QImage('./images/logo_bg.png')))
        self.pushButton_2.clicked.connect(self.reg_action)  # 点击按钮之后关闭窗口

    def reg_action(self):
        reg_dialog.show()

    def adj_login(self, user, pwd):
        return True

    def slot_ok(self):
        user = self.lineEdit.text()
        pwd = self.lineEdit_2.text()
        if self.adj_login(user, pwd) == False:
            win32api.MessageBox(0, "用户名或密码不正确,请重新输入!", "登录提醒", win32con.MB_ICONWARNING)
        else:
            self.close()

'''
登录对话框
'''
class regDialog(QtWidgets.QDialog, Ui_regedit):
    def __init__(self):
        super(regDialog, self).__init__()
        self.setupUi(self)
        self.label.setPixmap(QPixmap.fromImage(QImage('./images/logo_bg.png')))

    def save_reg_info(self, user, pwd):
       return True

    def slot_ok(self):
        user = self.user_lineEdit.text()
        pwd = self.pwd_lineEdit.text()
        if user == '' or pwd == '':
            win32api.MessageBox(0, "用户名或密码不能为空,请重新输入!", "注册提醒", win32con.MB_ICONWARNING)
        else:
            self.save_reg_info(user, pwd)
            self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    reg_dialog = regDialog()
    login_dialog = loginDialog()
    login_dialog.show()

    sys.exit(app.exec_())