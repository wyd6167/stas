from ui.login import Ui_login_ui
from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from PyQt5 import QtWidgets
from view import login,main as mainwindow
from view.splash import SplashScreen
from loguru import logger
from playhouse.shortcuts import model_to_dict
from models.user import User
from controller.main_controller import Main_controller
from PyQt5.QtCore import *
class Login_controller():
    def __init__(self):
        logger.info('系统启动')
        # splash = SplashScreen()  # 启动界面
        # splash.loadProgress()  # 启动界面
        self.main_controller=Main_controller()
        # self.main_view=mainwindow.MyPyQT_Form()
        self.login_view=login.MyPyQT_Form()
        self.login_view.startAnimation()
        self.login_view.initQSS()
        self.login_view.show()
        self.login_view.okButton.clicked.connect(lambda: self.login_pushButton_event())
        self.login_view.cancelButton.clicked.connect(self.close_event)
        # self.login_view.pushButton_2.clicked.connect(self.login_view.showMinimized)
    def login_pushButton_event(self):
        logger.info('正在登录')
        # self.main_controller.show_user()
        # self.main_controller.show_admin()
        # 登录的逻辑写在这里
        user_name = self.login_view.lineEditUser.text()
        password = self.login_view.lineEditPwd.text()
        if user_name == "" or password == "":
            QMessageBox.information(self.login_view, "错误提示", "请输入用户名密码")
            return
        info = User.select_from_user_name_and_password(user_name, password)
        if info is not None:
            if info.type==2:
                #admin 123456
                logger.info('管理员登录')
                QMessageBox.information(self.login_view, "登录成功", "欢迎管理员：\n" + str(info.user_name))
                self.login_view.close()
                self.main_controller.show_admin()
            # 登录成功
            else:
                logger.info('用户登录')
                QMessageBox.information(self.login_view, "登录成功", "欢迎用户：\n" + str(info.user_name)
                                        + "\n" + str(model_to_dict(info)))
                self.login_view.close()
                self.main_controller.show_user()

        else:
            QMessageBox.information(self.login_view, "错误提示", "用户名密码错误，请重试")
    def close_event(self):
        logger.info("关闭登录窗口")
        # 退出应用程序
        QApplication.instance().quit()

