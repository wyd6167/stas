# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI_login.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_login(object):
    def setupUi(self, login):
        login.setObjectName("login")
        login.resize(522, 271)
        login.setStyleSheet("background-color: rgb(78, 85, 92);")
        self.lineEdit = QtWidgets.QLineEdit(login)
        self.lineEdit.setGeometry(QtCore.QRect(270, 40, 221, 35))
        self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(login)
        self.lineEdit_2.setGeometry(QtCore.QRect(270, 110, 221, 35))
        self.lineEdit_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(login)
        self.pushButton.setGeometry(QtCore.QRect(270, 170, 221, 35))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setKerning(True)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(102, 227, 255, 255), stop:1 rgba(137, 59, 245, 255));\n"
"color: rgb(255, 255, 255);\n"
"font: 12pt \"微软雅黑\";")
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(login)
        self.label.setGeometry(QtCore.QRect(0, 0, 231, 271))
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(login)
        self.label_2.setGeometry(QtCore.QRect(270, 10, 54, 31))
        self.label_2.setStyleSheet("font: 12pt \"微软雅黑\";\n"
"color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(login)
        self.label_3.setGeometry(QtCore.QRect(270, 80, 61, 21))
        self.label_3.setStyleSheet("font: 12pt \"微软雅黑\";\n"
"color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
        self.pushButton_2 = QtWidgets.QPushButton(login)
        self.pushButton_2.setGeometry(QtCore.QRect(270, 220, 221, 35))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setKerning(True)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 12pt \"微软雅黑\";\n"
"background-color: rgb(154, 154, 154);")
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(login)
        self.pushButton.clicked.connect(login.slot_ok)
        QtCore.QMetaObject.connectSlotsByName(login)

    def retranslateUi(self, login):
        _translate = QtCore.QCoreApplication.translate
        login.setWindowTitle(_translate("login", "系统登录"))
        self.lineEdit.setText(_translate("login", "admin"))
        self.lineEdit_2.setText(_translate("login", "123456"))
        self.pushButton.setText(_translate("login", "登录"))
        self.label_2.setText(_translate("login", "用户名："))
        self.label_3.setText(_translate("login", "密   码："))
        self.pushButton_2.setText(_translate("login", "注册"))