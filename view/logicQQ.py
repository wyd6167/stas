import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import Qt

from PyQt5.Qt import QWidget, QPixmap, QPalette, QBrush, QLabel, QIcon
from PyQt5 import QtCore, QtGui, QtWidgets
# from contact.Main import MainWindow
from contact.View.component.Toast import Toast
import pymysql
from view.StyleSheet import StyleSheet

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        # Dialog.resize(1774, 887)
        Dialog.resize(1774, 971)
        self.move(100, 50)
        self.loginBg = QLabel(Dialog)
        self.accountcomboBox = QtWidgets.QLineEdit(Dialog)
        self.accountcomboBox.setObjectName("accountcomboBox")
        self.passwordEdit = QtWidgets.QLineEdit(Dialog)
        self.passwordEdit.setObjectName("passwordEdit")
        self.passwordError = QtWidgets.QLabel(Dialog)
        self.passwordError.setObjectName("passwordError")
        self.passwordError.setText("密码错误，请重新输入")
        self.loginBtn = QtWidgets.QPushButton(Dialog)
        self.loginBtn.setObjectName("loginBtn")
        print("賬號&密碼"
              "username:admin\n"
              "password:123456")
        self.codeBtn = QtWidgets.QPushButton(Dialog)
        self.codeBtn.setText("")
        self.codeBtn.setObjectName("codeBtn")
        self.codeBtn.setGeometry(QtCore.QRect(1690, 15, 50, 50))
        self.codeBtn.setIconSize(QtCore.QSize(50, 50))
        self.codeBtn.setIcon(QIcon(r".\dy\resource\loginClose.png"))
        self.codeBtn.setStyleSheet('QPushButton{ background: rgba(0,0,0,0.5);border-radius: 24px;}')
        #
        loginX = 1100
        loginY = 320

        self.accountcomboBox.setGeometry(QtCore.QRect(loginX, loginY, 280, 30))
        self.accountcomboBox.setPlaceholderText('用户名')
        self.passwordEdit.setGeometry(QtCore.QRect(loginX, loginY + 40, 280, 30))
        self.passwordError.setGeometry(QtCore.QRect(loginX, loginY + 75, 280, 30))
        self.passwordError.setStyleSheet("""
        QLabel{
            background: transparent;
            color:#fff;
        }
        """)
        self.passwordError.hide()
        self.passwordEdit.setPlaceholderText('密码')
        self.passwordEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.loginBtn.setGeometry(QtCore.QRect(loginX, loginY + 104, 280, 30))
        self.loginBg.setGeometry(QtCore.QRect(loginX - 70, loginY - 50, 400, 240))

        self.loginBg.setStyleSheet('QLabel{background: rgba(0,0,0,0.5);border-radius: 10px;}')

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.codeBtn.clicked.connect(self.close)
        self.loginBtn.clicked.connect(self.login_check)

    def jump(self):
        from controller.main_controller import Main_controller

        mainWindow = MainWindow()
        mainWindow.setStyleSheet(StyleSheet)
        mainWindow.show()
        self.close()

    def login_check(self):
        account = self.accountcomboBox.text()
        password = self.passwordEdit.text()
        # db = pymysql.connect(host='localhost',
        #                      user='root',
        #                      password='root@2022',
        #                      database='system2022')
        # cursor = db.cursor()
        # sql = "SELECT * FROM t_user"
        # cursor.execute(sql)
        # results = cursor.fetchall()
        # for row in results:
        #     nameRes = row[0]
        #     passwordRes = row[1]
        #     if account == nameRes and password == passwordRes:
        #         self.jump()
        #         return
        #     elif account == nameRes and password != passwordRes:
        #         self.passwordError.show()
        #         return
        if account=='wyd' and password=='123':
            self.jump()
            return

        # dy 再加一层判断
        toast = Toast()
        toast.make_text(QtCore.QPointF(1000, 500), "用户不存在", 3)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "登录"))
        # self.remembercheckBox.setText(_translate("Dialog", "记住密码"))
        # self.autoLogincheckBox.setText(_translate("Dialog", "自动登录"))
        self.loginBtn.setText(_translate("Dialog", "登录"))
        # self.registerBtn.setText(_translate("Dialog", "注册账号"))
        # self.forgotBtn.setText(_translate("Dialog", "找回密码"))


class LoginWin(QWidget, Ui_Dialog):
    def __init__(self, parent=None):
        super(LoginWin, self).__init__(parent)
        self.setupUi(self)

        self.initUI()
        self.center()

    def initUI(self):
        # self.setWindowFlags(QtCore.Qt.WindowMinimizeButtonHint)
        self.setWindowFlags(Qt.FramelessWindowHint)  # 去掉标题栏

    def center(self):
        # 获取屏幕的尺寸信息
        screen = QtWidgets.QDesktopWidget().screenGeometry()
        # 获取窗口的尺寸信息
        size = self.geometry()
        # 将窗口移动到指定位置
        self.move((screen.width() - size.width()) / 2, (screen.height() - size.height()) / 2)

def main():
    win = LoginWin()
    palette = QPalette()
    pix = QPixmap(r".\dy\resource\loginBg.png")

    pix = pix.scaled(win.width(), win.height())

    palette.setBrush(QPalette.Background, QBrush(pix))
    win.setPalette(palette)
    # win.setWindowFlags(QtCore.Qt.WindowMinimizeButtonHint)
    win.setWindowIcon(QIcon(r".\dy\resource\loginWindow.png"))

    win.show()


def main():
    app = QApplication(sys.argv)
    win = LoginWin()
    palette = QPalette()
    pix = QPixmap(r".\dy\resource\loginBg.png")

    pix = pix.scaled(win.width(), win.height())

    palette.setBrush(QPalette.Background, QBrush(pix))
    win.setPalette(palette)
    # win.setWindowFlags(QtCore.Qt.WindowMinimizeButtonHint)
    win.setWindowIcon(QIcon(r".\dy\resource\loginWindow.png"))

    win.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()