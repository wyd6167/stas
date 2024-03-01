import sys
from PyQt5.QtWidgets import QApplication, QMainWindow,QDateTimeEdit, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget, QHBoxLayout, QFormLayout, QGroupBox, QTableWidget, QTableWidgetItem, QMessageBox,QGridLayout
from PyQt5.QtGui import QIcon


class MedicalRecordManagement(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("病历信息管理")
        self.setGeometry(100, 100, 1000, 500)

        self.init_ui()

        self.patient_data = [
            ["1", "张三", "男", "35", "OP123", "IP456", "101", "P789", "医院A", "科室A", "医生A", "2022-01-01", "头部", "感冒",
             "正常"],
            ["2", "李四", "女", "45", "OP456", "IP789", "102", "P890", "医院B", "科室B", "医生B", "2022-01-02", "腹部", "胃炎",
             "异常"],
            ["3", "王五", "男", "55", "OP789", "IP123", "103", "P901", "医院C", "科室C", "医生C", "2022-01-03", "胸部", "心脏病",
             "正常"]
        ]

    def init_ui(self):
        # 创建界面元素
        self.id_label = QLabel("患者ID:")
        self.id_edit = QLineEdit()
        self.id_edit.setFixedWidth(200)

        self.name_label = QLabel("姓名:")
        self.name_edit = QLineEdit()
        self.name_edit.setFixedWidth(200)

        self.gender_label = QLabel("性别:")
        self.gender_edit = QLineEdit()
        self.gender_edit.setFixedWidth(200)

        self.age_label = QLabel("患者年龄:")
        self.age_edit = QLineEdit()
        self.age_edit.setFixedWidth(200)

        self.outpatient_label = QLabel("门诊号:")
        self.outpatient_edit = QLineEdit()
        self.outpatient_edit.setFixedWidth(200)

        self.inpatient_label = QLabel("住院号:")
        self.inpatient_edit = QLineEdit()
        self.inpatient_edit.setFixedWidth(200)

        self.bed_label = QLabel("床号:")
        self.bed_edit = QLineEdit()
        self.bed_edit.setFixedWidth(200)

        self.pathology_label = QLabel("病理号:")
        self.pathology_edit = QLineEdit()
        self.pathology_edit.setFixedWidth(200)

        self.hospital_label = QLabel("送检医院:")
        self.hospital_edit = QLineEdit()
        self.hospital_edit.setFixedWidth(200)

        self.department_label = QLabel("送检科室:")
        self.department_edit = QLineEdit()
        self.department_edit.setFixedWidth(200)

        self.doctor_label = QLabel("送检医师:")
        self.doctor_edit = QLineEdit()
        self.doctor_edit.setFixedWidth(200)

        self.date_label = QLabel("送检日期:")
        self.date_edit = QDateTimeEdit()
        self.date_edit.setDisplayFormat("yyyy-MM-dd HH:mm:ss")  # 设置日期时间格式
        self.date_edit.setFixedWidth(200)

        self.position_label = QLabel("取材部位:")
        self.position_edit = QLineEdit()
        self.position_edit.setFixedWidth(200)
        self.diagnosis_label = QLabel("临床诊断:")

        self.diagnosis_edit = QLineEdit()
        self.diagnosis_edit.setFixedWidth(200)

        self.appearance_label = QLabel("肉眼所见:")
        self.appearance_edit = QLineEdit()
        self.appearance_edit.setFixedWidth(200)
        self.add_button = QPushButton(QIcon('add_icon.png'), "添加")
        self.delete_button = QPushButton(QIcon('delete_icon.png'), "删除")
        self.update_button = QPushButton(QIcon('update_icon.png'), "更新")
        self.search_button = QPushButton(QIcon('search_icon.png'), "搜索")
        self.add_button.setFixedWidth(50)
        self.delete_button.setFixedWidth(50)
        self.update_button.setFixedWidth(50)
        self.search_button.setFixedWidth(50)
        self.table = QTableWidget()
        self.table.setColumnCount(13)
        self.table.setHorizontalHeaderLabels(
            ["患者ID", "姓名", "性别", "患者年龄", "门诊号", "住院号", "床号", "病理号", "送检医院", "送检科室", "送检医师", "送检日期", "取材部位"])

        # 创建布局
        form_layout_left = QFormLayout()
        form_layout_left.addRow(self.id_label, self.id_edit)
        form_layout_left.addRow(self.name_label, self.name_edit)
        form_layout_left.addRow(self.gender_label, self.gender_edit)
        form_layout_left.addRow(self.age_label, self.age_edit)
        form_layout_left.addRow(self.outpatient_label, self.outpatient_edit)
        form_layout_left.addRow(self.inpatient_label, self.inpatient_edit)
        form_layout_left.addRow(self.bed_label, self.bed_edit)

        form_layout_right = QFormLayout()
        form_layout_right.addRow(self.pathology_label, self.pathology_edit)
        form_layout_right.addRow(self.hospital_label, self.hospital_edit)
        form_layout_right.addRow(self.department_label, self.department_edit)
        form_layout_right.addRow(self.doctor_label, self.doctor_edit)
        form_layout_right.addRow(self.date_label, self.date_edit)
        form_layout_right.addRow(self.position_label, self.position_edit)

        form_layout_bottom = QFormLayout()
        form_layout_bottom.addRow(self.diagnosis_label, self.diagnosis_edit)
        form_layout_bottom.addRow(self.appearance_label, self.appearance_edit)

        button_layout = QHBoxLayout()
        button_layout.addWidget(self.add_button)
        button_layout.addWidget(self.delete_button)
        button_layout.addWidget(self.update_button)
        button_layout.addWidget(self.search_button)

        main_layout = QVBoxLayout()

        group_box_left = QGroupBox("基本信息")
        group_box_left.setLayout(form_layout_left)

        group_box_right = QGroupBox("送检信息")
        group_box_right.setLayout(form_layout_right)

        group_box_bottom = QGroupBox("其他信息")
        group_box_bottom.setLayout(form_layout_bottom)

        main_layout.addWidget(group_box_left)
        main_layout.addWidget(group_box_right)
        main_layout.addWidget(group_box_bottom)
        main_layout.addLayout(button_layout)
        # main_layout.addWidget(self.table)

        main_layout1 = QHBoxLayout()
        main_layout1.addLayout(main_layout)
        main_layout1.addWidget(self.table)
        self.table.setFixedWidth(900)
        central_widget = QWidget()
        central_widget.setLayout(main_layout1)
        self.setCentralWidget(central_widget)

        # 连接按钮的信号和槽
        self.add_button.clicked.connect(self.add_patient)
        self.delete_button.clicked.connect(self.delete_patient)
        self.update_button.clicked.connect(self.update_patient)
        self.search_button.clicked.connect(self.search_patient)

    def add_patient(self):
        patient_id = self.id_edit.text()
        name = self.name_edit.text()
        gender = self.gender_edit.text()
        age = self.age_edit.text()
        outpatient = self.outpatient_edit.text()
        inpatient = self.inpatient_edit.text()
        bed = self.bed_edit.text()
        pathology = self.pathology_edit.text()
        hospital = self.hospital_edit.text()
        department = self.department_edit.text()
        doctor = self.doctor_edit.text()
        date = self.date_edit.text()
        position = self.position_edit.text()

        if not patient_id or not name or not gender or not age or not outpatient or not inpatient or not bed \
                or not pathology or not hospital or not department or not doctor or not date or not position:
            QMessageBox.warning(self, "警告", "请填写完整的患者信息！")
            return

        new_patient = [patient_id, name, gender, age, outpatient, inpatient, bed, pathology, hospital, department,
                       doctor, date, position]
        self.patient_data.append(new_patient)
        self.update_table()

    def delete_patient(self):
        current_row = self.table.currentRow()
        if current_row != -1:
            del self.patient_data[current_row]
            self.update_table()

    def update_patient(self):
        current_row = self.table.currentRow()
        if current_row != -1:
            patient_id = self.id_edit.text()
            name = self.name_edit.text()
            gender = self.gender_edit.text()
            age = self.age_edit.text()
            outpatient = self.outpatient_edit.text()
            inpatient = self.inpatient_edit.text()
            bed = self.bed_edit.text()
            pathology = self.pathology_edit.text()
            hospital = self.hospital_edit.text()
            department = self.department_edit.text()
            doctor = self.doctor_edit.text()
            date = self.date_edit.text()
            position = self.position_edit.text()

            if not patient_id or not name or not gender or not age or not outpatient or not inpatient or not bed \
                    or not pathology or not hospital or not department or not doctor or not date or not position:
                QMessageBox.warning(self, "警告", "请填写完整的患者信息！")
                return

            updated_patient = [patient_id, name, gender, age, outpatient, inpatient, bed, pathology, hospital,
                               department, doctor, date, position]
            self.patient_data[current_row] = updated_patient
            self.update_table()

    def search_patient(self):
        patient_id = self.id_edit.text()
        for i, patient in enumerate(self.patient_data):
            if patient[0] == patient_id:
                self.table.selectRow(i)
                return
        QMessageBox.warning(self, "提示", "未找到该患者！")

    def update_table(self):
        self.table.setRowCount(len(self.patient_data))
        for i, patient in enumerate(self.patient_data):
            for j, value in enumerate(patient):
                item = QTableWidgetItem(value)
                self.table.setItem(i, j, item)

        self.clear_inputs()

    def clear_inputs(self):
        self.id_edit.clear()
        self.name_edit.clear()
        self.gender_edit.clear()
        self.age_edit.clear()
        self.outpatient_edit.clear()
        self.inpatient_edit.clear()
        self.bed_edit.clear()
        self.pathology_edit.clear()
        self.hospital_edit.clear()
        self.department_edit.clear()
        self.doctor_edit.clear()
        self.date_edit.clear()
        self.position_edit.clear()
        self.diagnosis_edit.clear()
        self.appearance_edit.clear()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MedicalRecordManagement()
    window.show()
    sys.exit(app.exec_())
