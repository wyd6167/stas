from ui.show_result import Ui_Form
from ui.MainWindow_resulr import Ui_MainWindow
from loguru import logger
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtGui import QMouseEvent, QColor, QPalette
from PyQt5.QtCore import Qt, QPoint
from utils.connect_mysql import db
from models.user import User
from PyQt5.QtWidgets import QFrame, QMessageBox, QTableWidgetItem, QApplication, QHeaderView,QMainWindow,QFileDialog,QGraphicsRectItem,QGraphicsView,QGraphicsScene,QGraphicsPolygonItem
import xlwt,xlrd,xlutils
from PyQt5.QtCore import Qt, QRectF
from PyQt5.QtGui import QBrush, QColor
import os
from xlutils.copy import copy
from ui.drawrect import InteractiveGraphicsRectItem
from ui.drawqpoly import PolygonAnnotation as InteractivePolygon
from ui.drawqpoly import AnnotationScene
from playhouse.shortcuts import model_to_dict
from PyQt5.QtGui import QPixmap
import cv2
from PyQt5.Qt import QSize, QImageReader
from PyQt5.QtGui import QImage, QPixmap, QPainter, QPen ,QPolygon
from PyQt5.QtCore import QRect, Qt,QPointF
from view.mylabel import MyLabel
from utils.algorithm.get_contour import get_contour
from view.MyQGraphicsView import MyGraphicsView
from view.StyleSheet import StyleSheet

class MyPyQT_Form(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MyPyQT_Form, self).__init__()
        self.setupUi(self)
        self.setStyleSheet(StyleSheet)
        # self.setWindowFlag(Qt.FramelessWindowHint)
        # self.setAttribute(Qt.WA_TranslucentBackground)
        # 按钮事件绑定
        self.pixmap = QPixmap('E:/stas/read_16/1/1637460-G.png')
        img = QImageReader('E:/stas/read_16/1/1637460-G.png')
        self.flag = False
        self.groupBox.resize(img.size().width(), img.size().height())
        self.label.resize(img.size().width(), img.size().height())

        self.label.setPixmap(self.pixmap)

        self.label_w = self.label.width()
        self.label_x = self.label.x()
        self.label_y = self.label.y()
        self.label_h = self.label.height()
        self.movex = ""
        self.movey = ""
        self.qScrollArea = self.qScrollArea

        self.resize_point = 10
        self.cur_img = cv2.imread('E:/stas/read_16/1/1637460-G.png')
        self.contour = get_contour(r'F:\python\mypy1\stas_system\stas_system\result\1637460-G.png')
        # self.contours=[QPoint(0,0),QPoint(0,25),QPoint(1,35),QPoint(5,96),QPoint(555,555)]
        self.list_contour=[]
        for c in self.contour[0]:
            self.list_contour.append(QPoint(c[0][0],c[0][1]))
        self.contours = QPolygon(self.list_contour)
        self.contours_interct = InteractivePolygon(QtGui.QPolygonF(self.list_contour))
        # self.contours_interct = InteractivePolygon()

        self.view = MyGraphicsView(self.label)
        self.view.setLabel(self.label)
        self.view.setPar(self)
        # self.view.setGeometry(0, 0, 1361, 901)
        self.view.setGeometry(0, 0, self.label.width(), self.label.height())

        self.view.setStyleSheet("background: transparent;")
        # self.view.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.view.setRenderHint(QPainter.Antialiasing)  # 设置抗锯齿渲染
        self.view.setTransformationAnchor(QGraphicsView.AnchorUnderMouse)
        self.view.setResizeAnchor(QGraphicsView.AnchorUnderMouse)
        # self.view.setDragMode(QGraphicsView.ScrollHandDrag)  # 设置拖拽模式为手型拖拽

        self.view.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)  # 关闭水平滚动条
        self.view.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)  # 关闭垂直滚动条
        self.scene = AnnotationScene(self.label)
        self.scene.setSceneRect(QRectF(0, 0, self.label.width(), self.label.height()))

        self.scene.addItem(self.contours_interct)
        self.scene.setPolyon(self.contours_interct)
        i=0

        # for point in self.list_contour:
        #     # if i > 0.9 * len(self.list_contour):
        #     if i % 2 == 0 or i %3==0 or i%7 == 0:
        #         # self.contours_interct.removeLastPoint()
        #         # self.contours_interct.addPoint(QPointF(point))
        #         self.contours_interct.addPoint(QPointF(point))
        #
        #     i+=1
        self.view.setScene(self.scene)
        self.label.setView(self.view)
        self.label.setPar(self)
        self.label.setScene(self.scene)
        # 创建矩形框
        # parent_item = QGraphicsRectItem(0, 0, 400, 400)
        # self.scene.addItem(parent_item)
        self.rect_item = InteractiveGraphicsRectItem(QRectF(0, 0, 200 * 2, 200 * 2),5)
        # self.rect_item.setPos(100,50)
        # self.rect_item.setX(10)
        # self.rect_item.setY(50)
        self.rect_item.setFlag(QGraphicsRectItem.ItemIsMovable, True)
        self.rect_item.setFlag(QGraphicsRectItem.ItemIsSelectable, True)
        self.rect_item.setFlag(QGraphicsRectItem.ItemSendsGeometryChanges, True)
        # self.rect_item.setBrush(QBrush(QColor(255, 0, 0)))
        self.rect_item.setZValue(1)
        self.scene.addItem(self.rect_item)
        text_item = self.scene.addWidget(self.label)
        text_item.setFlag(text_item.ItemIsMovable)  # 允许移动QLabel

        self.view.show()
        self.rectangle = []
        # self.rectangle.append([100,500,500,500])
        # self.rectangle.append([100,100,60,60])
        # self.rectangle.append([953.578128*2,262.81249*2,3.531248*2,2.75*2])
        # self.rectangle.append([265.578128*2,950.812496*2,3.531248*2,2.75*2])
        # self.rectangle.append([256 * 2, 944 * 2, 20 * 2, 20 * 2])
        self.rectangle_list = []
        for item in self.rectangle:
            self.rectangle_list.append(item)

        self.open_file.clicked.connect(lambda: self.handle_menu(self.handle_menu(self.open_file)))
        self.open_dir.clicked.connect(lambda: self.handle_menu(self.handle_menu(self.open_dir)))
        self.save.clicked.connect(lambda: self.handle_menu(self.handle_menu(self.save)))
        self.save_info.clicked.connect(lambda: self.handle_menu(self.handle_menu(self.save_info)))
        self.clear_all.clicked.connect(lambda: self.handle_menu(self.handle_menu(self.clear_all)))
        # self.hide_bingli.clicked.connect(lambda: self.hide_info())
        self.unload_drawing_Button.clicked.connect(lambda: self.handle_menu(self.handle_menu(self.unload_drawing_Button)))
        self.paint_rect.clicked.connect(lambda: self.modifyFlag())
        self.mouse.clicked.connect(lambda: self.modifyFlag_mouse())
        from functools import partial
        self.scene.setCurrentInstruction(0)
        QtWidgets.QShortcut(QtCore.Qt.Key_Escape, self, activated=partial(self.scene.setCurrentInstruction, 0))

    def handle_menu(self, menu):
        if menu == self.open_file or menu == self.unload_drawing_Button:
            self.click_openfile()
        elif menu == self.open_dir:
            dir_path = QFileDialog.getExistingDirectory(self, "选取文件夹", "./") + "/"

        elif menu == self.save :
            self.saveImage()
        elif menu == self.clear_all:
            self.name_Edit.setText("")
            self.age_Edit.setText("")
            self.patient_num_Edit.setText("")
            self.admission_num_Edit.setText("")
            self.bed_num_Edit.setText("")
            self.bingli_num_Edit.setText("")
            self.hospital_Edit.setText("")
            self.department_Edit.setText("")
            self.doctor_Edit.setText("")
            self.based_site_Edit.setText("")
            self.clinical_diagnosis_Edit.setText("")
            self.surface_Edit.setText("")
        elif menu == self.save_info:
            #wb=xlwt.Workbook()
            #ws = wb.add_sheet("Sheet")
            data = xlrd.open_workbook("F:\\python\\mypy1\\Projects_requiredByTeacher\\demo1\\demo1\\patient_info.xls")
            table = data.sheets()[0]
            print(table.nrows)
            self.writeExcel(table.nrows, 0, self.name_Edit.toPlainText())
            self.writeExcel(table.nrows, 1, self.comboBox.currentText())
            self.writeExcel(table.nrows, 2, self.age_Edit.toPlainText())
            self.writeExcel(table.nrows, 3, self.patient_num_Edit.toPlainText())
            self.writeExcel(table.nrows, 4, self.admission_num_Edit.toPlainText())
            self.writeExcel(table.nrows, 5, self.bed_num_Edit.toPlainText())
            self.writeExcel(table.nrows, 6, self.bingli_num_Edit.toPlainText())
            self.writeExcel(table.nrows, 7, self.hospital_Edit.toPlainText())
            self.writeExcel(table.nrows, 8, self.department_Edit.toPlainText())
            self.writeExcel(table.nrows, 9, self.doctor_Edit.toPlainText())
            self.writeExcel(table.nrows, 10, self.dateEdit.date().toString(Qt.ISODate))
            self.writeExcel(table.nrows, 11, self.based_site_Edit.toPlainText())
            self.writeExcel(table.nrows, 12, self.clinical_diagnosis_Edit.toPlainText())
            self.writeExcel(table.nrows, 13, self.surface_Edit.toPlainText())
            QMessageBox.information(self, "提示", "保存完毕")
        elif menu == self.print_report:
            if self.currentIndex != -2:
                picture_map = self.pictures[self.currentIndex]
                if picture_map.value:
                    dir_path = QFileDialog.getExistingDirectory(self, "选取文件夹", "./") + "/"
                    if dir_path != "/":
                        picture = picture_map.value
                        result_dir = os.path.join(picture.get_dir(), picture.name)  # 病人检测结果的存放目录,检测结果以病人名字命令
                        excel_path = os.path.join(result_dir, 'result.xls')
                        writer = ExcelUtil(excel_path)
                        writer.write(picture)
                        report = ReportCreater(picture.file_path, "./res/MedicalReport.docx", excel_path, dir_path)
                        report.create_report()
                        QMessageBox.information(self, "提示", "打印完毕")
        elif menu == self.help:
            webbrowser.open(os.path.abspath("./res/help.docx"))

    def click_openfile(self):
        openfile_name, n = QFileDialog.getOpenFileName(self, '选择文件', "./", 'image files(*.jpg , *.png)')
        print(openfile_name)
        if len(openfile_name):
            # Image1 = QImage(str(openfile_name))
            # self.Image.setPixmap(QPixmap.fromImage(Image1))
            self.label.setPixmap(QtGui.QPixmap(str(openfile_name)))
            self.label.resize(self.Image.width(), self.Image.height())
    def modifyFlag(self):
        if self.paint_rect.isChecked():
            self.view.setFlag(1)
            self.view.setCursor(Qt.CrossCursor)  # 图片可以绘制
            self.paint_rect.setCheckable(True)
        else:

            self.view.setFlag(0)
            self.view.setCursor(Qt.PointingHandCursor)  # 图片可以绘制
            self.paint_rect.setCheckable(True)
        self.mouse.setCheckable(False)
    def modifyFlag_mouse(self):
        if self.mouse.isChecked():
            self.view.setFlag(2)
            self.view.setCursor(Qt.PointingHandCursor)  # 图片可以绘制
            self.mouse.setCheckable(True)
        else:

            self.view.setFlag(0)
            self.view.setCursor(Qt.PointingHandCursor)  # 图片可以绘制
            self.mouse.setCheckable(True)
        self.paint_rect.setCheckable(False)
    def writeExcel(self,row, col, str):
        rb = xlrd.open_workbook("F:\\python\\mypy1\\Projects_requiredByTeacher\\demo1\\demo1\\patient_info.xls", formatting_info=True)
        wb = copy(rb)
        ws = wb.get_sheet(0)
        ws.write(row, col, str)
        wb.save("F:\\python\\mypy1\\Projects_requiredByTeacher\\demo1\\demo1\\patient_info.xls")
    def saveImage(self):  # 保存图片到本地
        image = self.Image.pixmap().toImage()
        # print(type(image))
        # screen = QApplication.primaryScreen()
        # pix = screen.grabWindow(self.Image.winId())
        fd, type = QFileDialog.getSaveFileName(self, "保存图片", "", "*.jpg;;*.png;;All Files(*)")
        image.save(fd)
    def mousePressEvent(self, e: QMouseEvent):
        if e.buttons() == QtCore.Qt.LeftButton:
            self.flag = True

    def mouseReleaseEvent(self, e: QMouseEvent):  # 鼠标释放事件重写

        self.flag = False
        self.movex = ""
        self.movey = ""

    def mouseMoveEvent(self, e: QMouseEvent):
        tmph = self.qScrollArea.horizontalScrollBar()
        tmpv = self.qScrollArea.verticalScrollBar()
        if self.flag:
            self.x1 = e.x()
            self.y1 = e.y()
            if self.movex != "" and self.movey != "":
                self.label_x = self.label_x + (self.x1 - self.movex)
                self.label_y = self.label_y + (self.y1 - self.movey)
                tmph.setValue(tmph.value() + self.movex - self.x1)
                tmpv.setValue(tmpv.value() + self.movey - self.y1)
            self.movex = self.x1
            self.movey = self.y1

    def wheelEvent(self, e):
        self.angle = e.angleDelta() / 8
        self.angleY = self.angle.y()
        if self.angleY > 0:
            if self.resize_point >= 1 and self.resize_point <= 19:  # 此处的self.resize_point初始值为10，作为缩放系数
                self.resize_point += 1
        elif self.angleY < 0:
            if self.resize_point >= 2 and self.resize_point <= 20:
                self.resize_point -= 1
        x_1 = e.x()
        y_1 = e.y()

        x2 = (x_1 - self.label.x()) / self.label.width()  # 第一次鼠标坐标x比值
        y2 = (y_1 - self.label.y()) / self.label.height()  # 第一次鼠标坐标y比值
        x2_ = x_1 - self.label.x()
        y2_ = y_1 - self.label.y()
        # 由于cV2包得到图像并非是我们所需的图片对象，这里先是对图片宽高根据缩放系数进行改变，然后将图片转换为QImage对象，在转换为QPixmap对象
        self.cur_resimg = cv2.resize(self.cur_img, (
            (int(self.cur_img.shape[1] * self.resize_point / 10)),
            (int(self.cur_img.shape[0] * self.resize_point / 10))))
        img2 = cv2.cvtColor(self.cur_resimg, cv2.COLOR_BGR2RGB)  # 转RGB格式，以在Qlabel中显示
        QImage = QtGui.QImage(img2, self.cur_resimg.shape[1], self.cur_resimg.shape[0], 3 * self.cur_resimg.shape[1],
                              QtGui.QImage.Format_RGB888)
        self.pixmap = QtGui.QPixmap((QImage).scaled(self.cur_resimg.shape[1], self.cur_resimg.shape[0]))

        self.label_w = self.cur_resimg.shape[1]
        self.label_h = self.cur_resimg.shape[0]
        if int(x2) == 0 and int(y2) == 0:
            x3 = x2
            y3 = y2
            Lmx2 = x3 * self.label_w
            Lmy2 = y3 * self.label_h
            self.label_x = int(x_1 - Lmx2)
            self.label_y = int(y_1 - Lmy2)
            # self.groupBox.resize(self.label_w, self.label_h)

            # self.label.resize(self.label_w, self.label_h)

            # self.qScrollArea.setGeometry(QtCore.QRect(0, 0, self.label_w, self.label_h))
            self.groupBox.setGeometry(QtCore.QRect(0, 0, self.label_w, self.label_h))
            self.label.setGeometry(QtCore.QRect(0, 0, self.label_w, self.label_h))

            self.label.setPixmap(self.pixmap)
            # print(self.label_w,self.label.width())
            self.view.setGeometry(0, 0, self.label.width(), self.label.height())
            self.scene.setSceneRect(QRectF(0, 0, self.label.width(), self.label.height()))

            tmph = self.qScrollArea.horizontalScrollBar()
            tmpv = self.qScrollArea.verticalScrollBar()
            tmph.setValue(tmph.value() + Lmx2 - x_1)
            tmpv.setValue(tmpv.value() + Lmy2 - y_1)
            # 缩放时保持标注相对位置和大小不变
            self.list_contour = []
            for c in self.contour[0]:
                self.list_contour.append(QPoint(c[0][0]*(self.resize_point / 10), c[0][1]*(self.resize_point / 10)))
            self.contours = QPolygon(self.list_contour)

            self.rectangle_list = []
            for item in self.rectangle:
                self.rectangle_list.append([item[0]*(self.resize_point / 10),item[1]*(self.resize_point / 10),
                                            item[2]* (self.resize_point / 10),item[3]*(self.resize_point / 10)])

            self.paintEvent(e)
            self.paintRect()
    def paintEvent(self, event):
        # super().paintEvent(event)
        # rect = QRect(100, 100, 1000, 1000)
        painter = QPainter(self.label.pixmap())
        # painter.begin(self.label)
        painter.setPen(QPen(Qt.red, 2, Qt.SolidLine))
        # painter.pointPolygonTest()
        # print(self.contours.boundingRect())
        # print(self.contours.contains(QPoint(535,421)))
        # print(self.contours.at(0))
        # print(contour)
        # polygon = QPolygon()
        # print(self.contours)
        # painter.drawPolygon(self.contours)
        # for rec in self.rectangle_list:
        #     rect =  QRect(rec[0],rec[1],rec[2],rec[3])
        #
        #     painter.setPen(QPen(Qt.red, 2, Qt.SolidLine))
        #     painter.drawRect(rect)

        painter.end()
    def paintRect(self):

        self.scene.clear()
        for rec in self.rectangle_list:
            rect_item = InteractiveGraphicsRectItem(QRectF(rec[0], rec[1], rec[2], rec[3]), 5)
            self.scene.addItem(rect_item)
        self.contours_interct = InteractivePolygon(QtGui.QPolygonF(self.list_contour))
        self.scene.addItem(self.contours_interct)
        self.view.show()



if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    A1 = MyPyQT_Form()
    A1.show()
    sys.exit(app.exec_())
