# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_demo3.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_frmMain(object):
    def setupUi(self, frmMain):
        frmMain.setObjectName("frmMain")
        frmMain.resize(1200, 680)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(frmMain.sizePolicy().hasHeightForWidth())
        frmMain.setSizePolicy(sizePolicy)
        frmMain.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(frmMain)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.loginWin = QtWidgets.QWidget(self.centralwidget)
        self.loginWin.setGeometry(QtCore.QRect(260, 130, 700, 420))
        self.loginWin.setStyleSheet("QWidget[objectName=\"loginWin\"]{\n"
"    background-image: url(:/images/images/login_win_bg.png);\n"
"}")
        self.loginWin.setObjectName("loginWin")
        self.okButton = QtWidgets.QToolButton(self.loginWin)
        self.okButton.setGeometry(QtCore.QRect(350, 290, 320, 40))
        self.okButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.okButton.setObjectName("okButton")
        self.widgetUser = QtWidgets.QWidget(self.loginWin)
        self.widgetUser.setGeometry(QtCore.QRect(350, 110, 320, 40))
        self.widgetUser.setObjectName("widgetUser")
        self.lineEditUser = QtWidgets.QLineEdit(self.widgetUser)
        self.lineEditUser.setGeometry(QtCore.QRect(50, 2, 270, 35))
        self.lineEditUser.setObjectName("lineEditUser")
        self.widgetPwd = QtWidgets.QWidget(self.loginWin)
        self.widgetPwd.setGeometry(QtCore.QRect(350, 170, 320, 40))
        self.widgetPwd.setObjectName("widgetPwd")
        self.lineEditPwd = QtWidgets.QLineEdit(self.widgetPwd)
        self.lineEditPwd.setGeometry(QtCore.QRect(50, 2, 270, 35))
        self.lineEditPwd.setObjectName("lineEditPwd")
        self.labelWelcome = QtWidgets.QLabel(self.loginWin)
        self.labelWelcome.setGeometry(QtCore.QRect(40, 60, 151, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.labelWelcome.setFont(font)
        self.labelWelcome.setObjectName("labelWelcome")
        self.labelWelLine = QtWidgets.QLabel(self.loginWin)
        self.labelWelLine.setGeometry(QtCore.QRect(50, 110, 100, 5))
        self.labelWelLine.setText("")
        self.labelWelLine.setObjectName("labelWelLine")
        self.labelMenu1 = QtWidgets.QLabel(self.loginWin)
        self.labelMenu1.setGeometry(QtCore.QRect(40, 310, 54, 12))
        self.labelMenu1.setAlignment(QtCore.Qt.AlignCenter)
        self.labelMenu1.setObjectName("labelMenu1")
        self.line = QtWidgets.QFrame(self.loginWin)
        self.line.setGeometry(QtCore.QRect(120, 305, 5, 20))
        self.line.setLineWidth(1)
        self.line.setMidLineWidth(0)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.loginWin)
        self.line_2.setGeometry(QtCore.QRect(210, 305, 5, 20))
        self.line_2.setLineWidth(1)
        self.line_2.setMidLineWidth(0)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.labelMenu2 = QtWidgets.QLabel(self.loginWin)
        self.labelMenu2.setGeometry(QtCore.QRect(140, 310, 54, 12))
        self.labelMenu2.setAlignment(QtCore.Qt.AlignCenter)
        self.labelMenu2.setObjectName("labelMenu2")
        self.labelMenu3 = QtWidgets.QLabel(self.loginWin)
        self.labelMenu3.setGeometry(QtCore.QRect(230, 310, 54, 12))
        self.labelMenu3.setAlignment(QtCore.Qt.AlignCenter)
        self.labelMenu3.setObjectName("labelMenu3")
        self.line_3 = QtWidgets.QFrame(self.loginWin)
        self.line_3.setGeometry(QtCore.QRect(45, 110, 60, 5))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(self.loginWin)
        self.line_4.setGeometry(QtCore.QRect(510, 35, 5, 20))
        self.line_4.setLineWidth(1)
        self.line_4.setMidLineWidth(0)
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.pushButtonAcount = QtWidgets.QPushButton(self.loginWin)
        self.pushButtonAcount.setGeometry(QtCore.QRect(400, 35, 75, 23))
        self.pushButtonAcount.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButtonAcount.setObjectName("pushButtonAcount")
        self.pushButtonPhone = QtWidgets.QPushButton(self.loginWin)
        self.pushButtonPhone.setGeometry(QtCore.QRect(550, 35, 75, 23))
        self.pushButtonPhone.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButtonPhone.setObjectName("pushButtonPhone")
        self.radioButton = QtWidgets.QRadioButton(self.loginWin)
        self.radioButton.setGeometry(QtCore.QRect(360, 240, 21, 31))
        self.radioButton.setText("")
        self.radioButton.setObjectName("radioButton")
        self.label = QtWidgets.QLabel(self.loginWin)
        self.label.setGeometry(QtCore.QRect(390, 240, 281, 35))
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.pushButtonFoget = QtWidgets.QPushButton(self.loginWin)
        self.pushButtonFoget.setGeometry(QtCore.QRect(590, 350, 75, 23))
        self.pushButtonFoget.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButtonFoget.setObjectName("pushButtonFoget")
        frmMain.setCentralWidget(self.centralwidget)

        self.retranslateUi(frmMain)
        QtCore.QMetaObject.connectSlotsByName(frmMain)

    def retranslateUi(self, frmMain):
        _translate = QtCore.QCoreApplication.translate
        frmMain.setWindowTitle(_translate("frmMain", "系统登录"))
        self.okButton.setText(_translate("frmMain", "登录"))
        self.lineEditUser.setPlaceholderText(_translate("frmMain", "请输入帐号"))
        self.lineEditPwd.setPlaceholderText(_translate("frmMain", "请输入密码"))
        self.labelWelcome.setText(_translate("frmMain", "Welcome"))
        self.labelMenu1.setText(_translate("frmMain", "最新动态"))
        self.labelMenu2.setText(_translate("frmMain", "服务中心"))
        self.labelMenu3.setText(_translate("frmMain", "关于我们"))
        self.pushButtonAcount.setText(_translate("frmMain", "帐号登录"))
        self.pushButtonPhone.setText(_translate("frmMain", "手机登录"))
        self.label.setText(_translate("frmMain", "<html><head/><body><p><span style=\"color:black;\">我已认真审阅并同意</span><span style=\"color:blue;\">客户使用规范内容及相关协议及法律规定</span></p></body></html>"))
        self.pushButtonFoget.setText(_translate("frmMain", "忘记密码"))
import demo3.res_rc
