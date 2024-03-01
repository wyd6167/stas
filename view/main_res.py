import sys
import os
import json
import openpyxl
import xlwt,xlrd,xlutils
import webbrowser
from xlutils.copy import copy
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QDate, QTime, QDateTime
from PyQt5.QtGui import QIcon, QPixmap, QColor , QImage
from PyQt5.QtCore import QBasicTimer
from PyQt5.QtWidgets import QApplication, QMainWindow  # 导入PyQt模块
from shutil import copyfile,copy
from ui.MainWindow_resulr import Ui_MainWindow
from PyQt5.QtWidgets import QListView, QApplication, QMainWindow, QCheckBox, QAbstractItemView, QFileDialog, QAction, \
    QDesktopWidget, QMessageBox, QTableWidgetItem
class MyMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        desktop = QApplication.desktop()
        self.hide_flag=1
        self.step = 0
        self.setupUi(self)
        self.initial_event()
        self.right.clicked.connect(lambda: self.button_click(self.right))
        self.left.clicked.connect(lambda: self.button_click(self.left))
        self.Bottom.clicked.connect(lambda: self.button_click(self.Bottom))
        self.top.clicked.connect(lambda: self.button_click(self.top))
        self.pushButton.clicked.connect(lambda: self.button_click(self.pushButton))
        #self.open_file.clicked.connect(lambda: self.click_openfile())
        self.open_file.clicked.connect(lambda: self.handle_menu(self.handle_menu(self.open_file)))
        self.open_dir.clicked.connect(lambda: self.handle_menu(self.handle_menu(self.open_dir)))
        self.save.clicked.connect(lambda: self.handle_menu(self.handle_menu(self.save)))
        self.save_info.clicked.connect(lambda: self.handle_menu(self.handle_menu(self.save_info)))
        self.clear_all.clicked.connect(lambda: self.handle_menu(self.handle_menu(self.clear_all)))
        self.hide_bingli.clicked.connect(lambda: self.hide_info())
        self.unload_drawing_Button.clicked.connect(lambda: self.handle_menu(self.handle_menu(self.unload_drawing_Button)))
        self.Select_comboBox_3.activated[str].connect(lambda: self.conboBox_mode(self.Select_comboBox_3))
        #self.grade.clicked.connect(lambda: self.mark_grade())
        self.pbar.valueChanged.connect(self.mark_grade)
        self.sure_g.clicked.connect(lambda: self.sure_grade())
    #槽函数
    def mkdir(self,path):
        # 去除首位空格
        path = path.strip()
        # 去除尾部 \ 符号
        path = path.rstrip("\\")
        # 判断路径是否存在
        # 存在   True
        # 不存在  False
        isExists = os.path.exists(path)
        # 判断结果
        if not isExists:
            # 如果不存在则创建目录
             # 创建目录操作函数
            os.makedirs(path)
            print(path + ' 创建成功')
            return True
        else:
            print(path + ' 目录已存在')
            return False
    def sure_grade(self):
        print(self.pbar.value())
        with open("./record.json", "w") as f:
            json.dump(self.pbar.value(), f)
        mkpath = "F:\\python\\mypy1\\Projects_requiredByTeacher\\demo1\\demo1\\json_and_image\\1"
        if self.mkdir(mkpath):
            #copyfile("./record.json",mkpath)
            copy("./record.json",mkpath)
            image = self.Image.pixmap().toImage()
            image.save(mkpath+"\\1.png")
            QMessageBox.information(self, "提示", "打分成功",
                                    QMessageBox.Yes)
        else:
            QMessageBox.critical(self, "错误", "打分失败")

    def mark_grade(self):
        print("do action")
        self.grade.setNum(self.pbar.value())
        # self.step+=1
        # if self.step>10:
        #     self.step=0
        # self.pbar.setValue(self.step)
    def conboBox_mode(self,text):
        print(text.currentText())
    def saveImage(self):  # 保存图片到本地
        image=self.Image.pixmap().toImage()
        #print(type(image))
        # screen = QApplication.primaryScreen()
        # pix = screen.grabWindow(self.Image.winId())
        fd, type = QFileDialog.getSaveFileName(self, "保存图片", "", "*.jpg;;*.png;;All Files(*)")
        image.save(fd)
    def hide_info(self):
        if self.hide_flag==1:
            self.name.setHidden(True)
            self.name_Edit.setHidden(True)
            self.comboBox.setHidden(True)
            self.sex.setHidden(True)
            self.age.setHidden(True)
            self.age_Edit.setHidden(True)
            self.bingli_num.setHidden(True)
            self.hospital.setHidden(True)
            self.patient_num.setHidden(True)
            self.admission_num.setHidden(True)
            self.hospital_Edit.setHidden(True)
            self.patient_num_Edit.setHidden(True)
            self.admission_num_Edit.setHidden(True)
            self.bingli_num_Edit.setHidden(True)
            self.bed_num.setHidden(True)
            self.department.setHidden(True)
            self.doctor.setHidden(True)
            self.date.setHidden(True)
            self.bed_num_Edit.setHidden(True)
            self.department_Edit.setHidden(True)
            self.doctor_Edit.setHidden(True)
            self.dateEdit.setHidden(True)
            self.based_site.setHidden(True)
            self.clinical_diagnosis.setHidden(True)
            self.surface.setHidden(True)
            self.based_site_Edit.setHidden(True)
            self.clinical_diagnosis_Edit.setHidden(True)
            self.surface_Edit.setHidden(True)
            self.patient_infor.setHidden(True)
            self.unload_drawing.setHidden(True)
            self.unload_drawing_Button.setHidden(True)
            self.save_info.setHidden(True)
            self.clear_all.setHidden(True)
            #self.hide_bingli.setHidden(True)
            self.Image.setGeometry(QtCore.QRect(200, -10, 1361, 901))
            self.hide_flag=0
            self.hide_bingli.setText("显示")
            self.hide_bingli.setStyleSheet("background-image: url(:/resource/显示.png);\n"
                                           "")
            self.hide_bingli.setGeometry(QtCore.QRect(1750, 340, 23, 31))
        else:
            self.name.setHidden(False)
            self.name_Edit.setHidden(False)
            self.comboBox.setHidden(False)
            self.sex.setHidden(False)
            self.age.setHidden(False)
            self.age_Edit.setHidden(False)
            self.bingli_num.setHidden(False)
            self.hospital.setHidden(False)
            self.patient_num.setHidden(False)
            self.admission_num.setHidden(False)
            self.hospital_Edit.setHidden(False)
            self.patient_num_Edit.setHidden(False)
            self.admission_num_Edit.setHidden(False)
            self.bingli_num_Edit.setHidden(False)
            self.bed_num.setHidden(False)
            self.department.setHidden(False)
            self.doctor.setHidden(False)
            self.date.setHidden(False)
            self.bed_num_Edit.setHidden(False)
            self.department_Edit.setHidden(False)
            self.doctor_Edit.setHidden(False)
            self.dateEdit.setHidden(False)
            self.based_site.setHidden(False)
            self.clinical_diagnosis.setHidden(False)
            self.surface.setHidden(False)
            self.based_site_Edit.setHidden(False)
            self.clinical_diagnosis_Edit.setHidden(False)
            self.surface_Edit.setHidden(False)
            self.patient_infor.setHidden(False)
            self.unload_drawing.setHidden(False)
            self.unload_drawing_Button.setHidden(False)
            self.save_info.setHidden(False)
            self.clear_all.setHidden(False)
            # self.hide_bingli.setHidden(True)
            self.Image.setGeometry(QtCore.QRect(0, -10, 1361, 901))
            self.hide_flag = 1
            self.hide_bingli.setText("隐藏")
            self.hide_bingli.setStyleSheet("background-image: url(:/resource/隐藏.png);\n"
                                           "")
            self.hide_bingli.setGeometry(QtCore.QRect(1340, 340, 23, 31))

    def button_click(self,direction):
        if direction==self.left:
            print("left")
        elif direction==self.right:
            print("right")
        elif direction==self.Bottom:
            print("bottom")
        elif direction==self.top:
            print("top")
        else:
            print("person")
    def click_openfile(self):
        openfile_name,n = QFileDialog.getOpenFileName(self, '选择文件', "./", 'image files(*.jpg , *.png)')
        print(openfile_name)
        if len(openfile_name):
            #Image1 = QImage(str(openfile_name))
            #self.Image.setPixmap(QPixmap.fromImage(Image1))
            self.Image.setPixmap(QtGui.QPixmap(str(openfile_name)))
            self.Image.resize(self.Image.width(), self.Image.height())
        # dir_path就是选中的那个文件夹路径
    def fault_show_function(self):
        dialog_fault = QDialog()
        url_father = os.path.dirname(os.path.abspath(__file__))
        image_path = url_father + "/fault_information.png"
        pic = QPixmap(image_path)
        label_pic = QLabel("show", dialog_fault)
        label_pic.setPixmap(pic)
        label_pic.setGeometry(10,10,1019,537)
        dialog_fault.exec_()

    def writeExcel(self,row, col, str):
        rb = xlrd.open_workbook("F:\\python\\mypy1\\Projects_requiredByTeacher\\demo1\\demo1\\patient_info.xls", formatting_info=True)
        wb = copy(rb)
        ws = wb.get_sheet(0)
        ws.write(row, col, str)
        wb.save("F:\\python\\mypy1\\Projects_requiredByTeacher\\demo1\\demo1\\patient_info.xls")
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

            # ws.write(0, 1, "性别")
            # ws.write(0, 2, "年龄")
            # ws.write(0, 3, "门诊号")
            # ws.write(0, 4, "住院号")
            # ws.write(0, 5, "床号")
            # ws.write(0, 6, "病理号")
            # ws.write(0, 7, "送检医院")
            # ws.write(0, 8, "送检科室")
            # ws.write(0, 9, "送检医师")
            # ws.write(0, 10, "送检日期")
            # ws.write(0, 11, "取材部位")
            # ws.write(0, 12, "临床诊断")
            # ws.write(0, 13, "肉眼所见")
            #
            #wb.save('patient_info.xls')
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
    def initial_event(self):
        self.right.setStyleSheet(
            "QPushButton{border-image: url(:/resource/right.png);}"
                                 "\n"
                                 "QPushButton{background: transparent;}""QPushButton:pressed{border-image:url(./res/pass_file_new.png);}"
                                 )
        self.left.setStyleSheet(
            "QPushButton{border-image: url(:/resource/left.png);}"
            "\n"
            "QPushButton{background: transparent;}""QPushButton:pressed{border-image:url(./res/pass_file_new.png);}"
        )
        self.top.setStyleSheet(
            "QPushButton{border-image: url(:/resource/top.png);}"
            "\n"
            "QPushButton{background: transparent;}""QPushButton:pressed{border-image:url(./res/pass_file_new.png);}"
        )
        self.Bottom.setStyleSheet(
            "QPushButton{border-image: url(:/resource/bottom.png);}"
            "\n"
            "QPushButton{background: transparent;}""QPushButton:pressed{border-image:url(./res/pass_file_new.png);}"
        )
        self.pushButton.setStyleSheet("QPushButton{border-image: url(:/resource/重新2_t.png);}\n"
                                      "\n"
                                      "QPushButton{background: transparent;}"
                                      "QPushButton:pressed{border-image:url(./res/pass_file_new.png);}"
                                      "")


if __name__ == '__main__':
    app = QApplication(sys.argv)  # 使用sys新建一个应用（Application）对象
    mainWindow = MyMainWindow()  # 新建一个Qt中QMainWindow()类函数
    #testWindow = MyMainWindow()  # 定义testWindow，与我们创建的窗体绑定
    #testWindow.setupUi(mainWindow)  # 为mainWindow绑定窗体
    mainWindow.show()  # 将mainWindow窗体进行显示
    sys.exit(app.exec_())  # 进入主循环，事件开始处理，接收由窗口触发的事件