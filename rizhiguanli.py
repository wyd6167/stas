import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget, QLabel, QComboBox, QPushButton, QHBoxLayout, QHeaderView, QDateTimeEdit


class LogManagementApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('日志管理界面')
        self.setGeometry(100, 100, 800, 600)

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.setup_ui()

    def setup_ui(self):
        # 创建过滤器部分
        filter_layout = QHBoxLayout()

        label_filter = QLabel('过滤器:')
        filter_layout.addWidget(label_filter)

        combo_filter_type = QComboBox()
        combo_filter_type.addItem('所有操作类型')
        combo_filter_type.addItem('登录')
        combo_filter_type.addItem('注销')
        combo_filter_type.addItem('其他操作')
        filter_layout.addWidget(combo_filter_type)

        label_start_time = QLabel('开始时间:')
        filter_layout.addWidget(label_start_time)

        datetime_start = QDateTimeEdit(self)
        filter_layout.addWidget(datetime_start)

        label_end_time = QLabel('结束时间:')
        filter_layout.addWidget(label_end_time)

        datetime_end = QDateTimeEdit(self)
        filter_layout.addWidget(datetime_end)

        filter_button = QPushButton('应用过滤器')
        filter_button.clicked.connect(self.apply_filter)
        filter_layout.addWidget(filter_button)

        # 创建操作日志表格部分
        table_layout = QVBoxLayout()

        self.table_widget = QTableWidget(self)
        self.table_widget.setColumnCount(4)
        self.table_widget.setHorizontalHeaderLabels(['主键', '时间', '操作类型', '用户职称'])
        self.table_widget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        table_layout.addWidget(self.table_widget)

        # 主布局
        main_layout = QVBoxLayout()
        main_layout.addLayout(filter_layout)
        main_layout.addLayout(table_layout)

        self.central_widget.setLayout(main_layout)

    def apply_filter(self):
        # TODO: 实现应用过滤器的逻辑

        # 示例数据，实际情况中需要从数据库中获取
        sample_data = [
            {'主键': 1, '时间': '2024-01-30 10:30', '操作类型': '登录', '用户职称': '管理员'},
            {'主键': 2, '时间': '2024-01-30 11:45', '操作类型': '上传切片', '用户职称': '用户A'},
            {'主键': 3, '时间': '2024-01-30 12:15', '操作类型': '修改诊断结果', '用户职称': '用户B'},
        ]

        # 清空表格
        self.table_widget.setRowCount(0)

        # 添加数据到表格
        for row, log_entry in enumerate(sample_data):
            self.table_widget.insertRow(row)
            for col, value in enumerate(log_entry.values()):
                item = QTableWidgetItem(str(value))
                self.table_widget.setItem(row, col, item)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_app = LogManagementApp()
    main_app.show()
    sys.exit(app.exec_())
