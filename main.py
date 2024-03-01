import sys
from PyQt5 import QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from utils import global_var as gl, logs
from utils.connect_mysql import db
from ui.login import Ui_login_ui
from PyQt5 import QtCore
from controller import login_controller
QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
from utils import global_var
if __name__ == '__main__':
    logs.setting()
    db.connect()
    global_var.__init()
    global_var.set_value('进度',0)
    app = QtWidgets.QApplication(sys.argv)
    my_pyqt_form = login_controller.Login_controller()
    app.exec_()