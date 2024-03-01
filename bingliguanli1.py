import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget, QHBoxLayout, QFormLayout, QGroupBox, QTableWidget, QTableWidgetItem, QMessageBox
from PyQt5.QtGui import QIcon


class MedicalRecordManagement(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("病历信息管理")
        self.setGeometry(100, 100, 1000, 500)  # 调整窗口大小

        self.init_ui()

        self.patient_data = [
            ["1", "张三", "男", "35", "OP123", "IP456", "101", "P789", "医院A", "科室A", "医生A", "2022-01-01", "头部", "感冒", "正常"],
            ["2", "李四", "女", "45", "OP456", "IP789", "102", "P890", "医院B", "科室B", "医生B", "2022-01-02", "腹部", "胃炎", "异常"],
            ["3", "王五", "男", "55", "OP789", "IP123", "103", "P901", "医院C", "科室C", "医生C", "2022-01-03", "胸部", "心脏病", "正常"]
        ]

    def init_ui(self):
        # 创建界面元素
        self.id_label = QLabel("患者ID:")
        self.id_edit = QLineEdit()

        self.name_label = QLabel("姓名:")
        self.name_edit = QLineEdit()

        self.gender_label = QLabel("性别:")
        self.gender_edit = QLineEdit()

        self.age_label = QLabel("患者年龄:")
        self.age_edit = QLineEdit()

        self.outpatient_label = QLabel("门诊号:")
        self.outpatient_edit = QLineEdit()

        self.inpatient_label = QLabel("住院号:")
        self.inpatient_edit = QLineEdit()

        self.bed_label = QLabel("床号:")
        self.bed_edit = QLineEdit()

        self.pathology_label = QLabel("病理号:")
        self.pathology_edit = QLineEdit()

        self.hospital_label = QLabel("送检医院:")
        self.hospital_edit = QLineEdit()

        self.department_label = QLabel("送检科室:")
        self.department_edit = QLineEdit()

        self.doctor_label = QLabel("送检医师:")
        self.doctor_edit = QLineEdit()

        self.date_label = QLabel("送检日期:")
        self.date_edit = QLineEdit()

        self.position_label = QLabel("取材部位:")
        self.position_edit = QLineEdit()

        self.diagnosis_label = QLabel("临床诊断:")
        self.diagnosis_edit = QLineEdit()

        self.appearance_label = QLabel("肉眼所见:")
        self.appearance_edit = QLineEdit()

        self.add_button = QPushButton(QIcon('add_icon.png'), "添加")
        self.delete_button = QPushButton(QIcon('delete_icon.png'), "删除")
        self.update_button = QPushButton(QIcon('update_icon.png'), "更新")
        self.search_button = QPushButton(QIcon('search_icon.png'), "搜索")

        self.table = QTableWidget()
        self.table.setColumnCount(13)
        self.table.setHorizontalHeaderLabels(
            ["患者ID", "姓名", "性别", "患者年龄", "门诊号", "住院号", "床号", "病理号", "送检医院", "送检科室", "送检医师", "送检日期", "取材部位"])

        # 创建布局
        form_layout_top = QFormLayout()
        form_layout_top.addRow(self.id_label, self.id_edit)
        form_layout_top.addRow(self.gender_label, self.gender_edit)

        form_layout_bottom = QFormLayout()
        form_layout_bottom.addRow(self.outpatient_label, self.outpatient_edit)
        form_layout_bottom.addRow(self.bed_label, self.bed_edit)
        form_layout_bottom.addRow(self.hospital_label, self.hospital_edit)
        form_layout_bottom.addRow(self.doctor_label, self.doctor_edit)
        form_layout_bottom.addRow(self.position_label, self.position_edit)
        form_layout_bottom.addRow(self.appearance_label, self.appearance_edit)

        button_layout = QHBoxLayout()
        button_layout.addWidget(self.add_button)
        button_layout.addWidget(self.delete_button)
        button_layout.addWidget(self.update_button)
        button_layout.addWidget(self.search_button)

        main_layout = QVBoxLayout()

        group_box_top = QGroupBox("基本信息")
        group_box_top.setLayout(form_layout_top)

        group_box_bottom = QGroupBox("其他信息")
        group_box_bottom.setLayout(form_layout_bottom)

        main_layout.addWidget(group_box_top)
        main_layout.addLayout(button_layout)
        main_layout.addWidget(group_box_bottom)
        main_layout.addWidget(self.table)

        central_widget = QWidget()
        central_widget.setLayout(main_layout)
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
