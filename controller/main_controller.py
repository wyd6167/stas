from PyQt5.QtWidgets import *
from view import login,main as mainwindow,main_admin as main_adminwindow,show_result,DemoRoundProgress
from loguru import logger
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.Qt import QSize, QImageReader
import cv2
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtGui import QImage, QPixmap, QPainter, QPen
from PyQt5.QtCore import QRect, Qt,QThread,pyqtSignal
import time
from utils import global_var
from model.yolov7.detect_WSI import detect_one
from model.yolov7.detect_WSI import Detect
import threading
import os
from preprocess.Slide.openslide_func import read_svs
import traceback
class FindProgressThread(QtCore.QThread):
    result=False
    _signal = pyqtSignal(float)

    def __init__(self):
        super(FindProgressThread, self).__init__()

    def __del__(self):
        self.wait()
    def run(self):
        while True:
            time.sleep(1)
            self._signal.emit(global_var.get_value('进度'))
            if global_var.get_value('进度')==1:
                # self._signal.emit(global_var.get_value('进度'))  # 注意这里与_signal = pyqtSignal(str)中的类型相同
                break
        return

    def get_result(self):
        return self.result

class ProgressThread(QThread):
    signal = pyqtSignal()

    def run(self):
        svs = global_var.get_value('svs_path')
        detect = Detect()
        detect.detect_one(str(svs))
        self.signal.emit()

class Main_controller():
    def __init__(self):

        self.main_view=mainwindow.MyPyQT_Form()
        self.main_view_admin=main_adminwindow.MyPyQT_Form()
        self.main_view.pushButton.clicked.connect(self.close_event)
        self.main_view.pushButton_2.clicked.connect(self.main_view.showMinimized)
        self.main_view.pushButton_3.clicked.connect(self.single_upload_event)
        self.main_view.pushButton_4.clicked.connect(self.mutli_upload_event)
        self.show_result=show_result.MyPyQT_Form()
    def show_user(self):
        self.main_view.show()
    def show_admin(self):
        self.main_view_admin.show()
    def close_event(self):
        logger.info("关闭登录窗口")
        # 退出应用程序
        QApplication.instance().quit()
    def single_upload_event(self):
        logger.info("单张上传")
        get_filename_path, ok = QFileDialog.getOpenFileName(self.main_view,
                                                            "选取单个文件",
                                                            "E:\显微镜\qiqiangdata",
                                                            "All Files (*);;SVS Files (*.svs)")
        print(str(get_filename_path))
        try:
            if str(get_filename_path) is not None and len(str(get_filename_path))>0:
                self.main_view.hide()
                # global_var.set_value('进度',0)
                global_var.set_value('svs_path',get_filename_path)
                jiance = ProgressThread()

                jiance.signal.connect(self.close_progress)
                jiance.start()
                self.Progress=DemoRoundProgress.Progress("<a link='b'>正在测试</a>")
                self.Progress.show()

                filename=str(get_filename_path)
                _,extension = os.path.splitext(filename)
                print(extension)
                bili = 16
                if extension=='.svs':
                    svs= read_svs(filename, bili)
                    image_svs = QImage(svs.data, svs.shape[1],svs.shape[0], svs.shape[2]*svs.shape[1],QImage.Format_RGB888)
                    none,img_encoded = cv2.imencode('.png',svs)
                    self.show_result.cur_img=cv2.imread(filename)
                    self.show_result.cur_img=cv2.imdecode(img_encoded,cv2.IMREAD_COLOR)
                    self.pixmap = QPixmap.fromImage(image_svs)  # 按指定路径找到图片
                    self.show_result.groupBox.resize(self.pixmap.size().width(), self.pixmap.size().height())
                    self.show_result.label.resize(self.pixmap.size().width(), self.pixmap.size().height())
                    self.show_result.label.setPixmap(self.pixmap)
                    self.show_result.rectangle.clear()
                    # for c in self.show_result.contour[0]:
                    #     self.show_result.list_contour.append(QPoint(c[0][0]*(16/bili)), c[0][1]*(bili*(16/bili)))
                    txt_path = r'F:\python\mypy1\stas_system\stas_system\runs\detect\exp69\labels'
                    for root,dirs, files in os.walk(txt_path):
                        for file in files:
                            file_path = os.path.join(root, file)
                            print(file_path)

                            with open(file_path) as f:
                                zuobiao = f.readline().strip().split(' ')
                                print(zuobiao)
                                print(txt_path.split('\\')[-1])
                                x = (float(file_path.split('\\')[-1].split('_')[1]) + float(zuobiao[2])*512)/bili
                                y = (float(file_path.split('\\')[-1].split('_')[2].split('.')[0]) + float(zuobiao[1]) * 512) / bili
                                # x = (float(txt_path.split('\\')[-1].split('_')[1])) / 32
                                # y = (float(txt_path.split('\\')[-1].split('_')[2].split('.')[0])) / 32
                                width = (512 * float(zuobiao[3]))/bili
                                height = (512 * float(zuobiao[4]))/bili
                                # print(x,y,width,height)
                                # exit()

                            self.show_result.rectangle.append([y,x,width,height])
                            # self.show_result.paintEvent()
                            self.show_result.show()
        except Exception as e:
            traceback.print_exc()


    def mutli_upload_event(self):
        logger.info("批量上传")
        get_filename_path, ok = QFileDialog.getOpenFileNames(self.main_view,
                                                            "选取多个文件",
                                                            "E:/",
                                                            "All Files (*);;SVS Files (*.svs)")
        print(str(get_filename_path))
    def close_progress(self):
        self.Progress.close()
        self.Progress.destroy()
        self.main_view.show()
        filename = global_var.get_value('svs_path')
        svs = read_svs(filename, 32)
        image_svs = QImage(svs.data, svs.shape[1], svs.shape[0], svs.shape[2] * svs.shape[1], QImage.Format_RGB888)
        none, img_encoded = cv2.imencode('.png', svs)
        self.show_result.cur_img = cv2.imread(filename)
        self.show_result.cur_img = cv2.imdecode(img_encoded, cv2.IMREAD_COLOR)
        self.pixmap = QPixmap.fromImage(image_svs)  # 按指定路径找到图片
        self.show_result.groupBox.resize(self.pixmap.size().width(), self.pixmap.size().height())
        self.show_result.label.resize(self.pixmap.size().width(), self.pixmap.size().height())
        self.show_result.label.setPixmap(self.pixmap)
        self.show_result.show()

            # self.show_result.groupBox.resize(self.pixmap.size().width(), self.pixmap.size().height())
            # self.show_result.label.resize(self.pixmap.size().width(), self.pixmap.size().height())
            # self.show_result.label.setPixmap(self.pixmap)
            # self.show_result.show()

def jiance():

    while global_var.get_value('进度') == 0:
        pass
    return True