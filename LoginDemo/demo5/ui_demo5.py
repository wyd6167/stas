# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_demo5.ui'
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
        self.loginWin.setGeometry(QtCore.QRect(170, 120, 800, 450))
        self.loginWin.setStyleSheet("QWidget[objectName=\"loginWin\"]{\n"
"    background-image: url(:/images/images/login_win_bg1.png);\n"
"}")
        self.loginWin.setObjectName("loginWin")
        self.okButton = QtWidgets.QToolButton(self.loginWin)
        self.okButton.setGeometry(QtCore.QRect(530, 330, 171, 40))
        self.okButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.okButton.setObjectName("okButton")
        self.widgetUser = QtWidgets.QWidget(self.loginWin)
        self.widgetUser.setGeometry(QtCore.QRect(450, 120, 320, 40))
        self.widgetUser.setObjectName("widgetUser")
        self.lineEditUser = QtWidgets.QLineEdit(self.widgetUser)
        self.lineEditUser.setGeometry(QtCore.QRect(50, 2, 270, 35))
        self.lineEditUser.setObjectName("lineEditUser")
        self.widgetPwd = QtWidgets.QWidget(self.loginWin)
        self.widgetPwd.setGeometry(QtCore.QRect(450, 190, 320, 40))
        self.widgetPwd.setObjectName("widgetPwd")
        self.lineEditPwd = QtWidgets.QLineEdit(self.widgetPwd)
        self.lineEditPwd.setGeometry(QtCore.QRect(50, 2, 270, 35))
        self.lineEditPwd.setObjectName("lineEditPwd")
        self.labelWelLine = QtWidgets.QLabel(self.loginWin)
        self.labelWelLine.setGeometry(QtCore.QRect(50, 110, 100, 5))
        self.labelWelLine.setText("")
        self.labelWelLine.setObjectName("labelWelLine")
        self.radioButton = QtWidgets.QRadioButton(self.loginWin)
        self.radioButton.setGeometry(QtCore.QRect(460, 260, 21, 31))
        self.radioButton.setText("")
        self.radioButton.setObjectName("radioButton")
        self.label = QtWidgets.QLabel(self.loginWin)
        self.label.setGeometry(QtCore.QRect(490, 260, 281, 35))
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.labelTitle = QtWidgets.QLabel(self.loginWin)
        self.labelTitle.setGeometry(QtCore.QRect(530, 39, 161, 41))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(22)
        font.setBold(False)
        font.setWeight(50)
        self.labelTitle.setFont(font)
        self.labelTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.labelTitle.setObjectName("labelTitle")
        self.pushButtonReg = QtWidgets.QPushButton(self.loginWin)
        self.pushButtonReg.setGeometry(QtCore.QRect(580, 380, 75, 23))
        self.pushButtonReg.setObjectName("pushButtonReg")
        frmMain.setCentralWidget(self.centralwidget)

        self.retranslateUi(frmMain)
        QtCore.QMetaObject.connectSlotsByName(frmMain)

    def retranslateUi(self, frmMain):
        _translate = QtCore.QCoreApplication.translate
        frmMain.setWindowTitle(_translate("frmMain", "系统登录"))
        self.okButton.setText(_translate("frmMain", "登录"))
        self.lineEditUser.setPlaceholderText(_translate("frmMain", "请输入帐号"))
        self.lineEditPwd.setPlaceholderText(_translate("frmMain", "请输入密码"))
        self.label.setText(_translate("frmMain", "<html><head/><body><p><span style=\"color:black;\">我已认真审阅并同意</span><span style=\"color:blue;\">客户使用规范内容及相关协议及法律规定</span></p></body></html>"))
        self.labelTitle.setText(_translate("frmMain", "系统登录"))
        self.pushButtonReg.setText(_translate("frmMain", "立即注册"))
import demo5.res_rc
