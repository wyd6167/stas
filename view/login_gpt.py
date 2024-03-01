import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout
from PyQt5.QtGui import QIcon

class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("登录")
        self.resize(500, 300)  # 设置窗口大小
        self.setWindowIcon(QIcon('icon.png'))

        # 设置背景颜色
        self.setStyleSheet("background-color: #f2f2f2;")

        self.username_label = QLabel("用户名:")
        self.password_label = QLabel("密码:")

        self.username_input = QLineEdit()
        self.username_input.setStyleSheet("background-color: #ffffff;")
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.Password)
        self.password_input.setStyleSheet("background-color: #ffffff;")

        self.user_login_button = QPushButton("用户登录")
        self.user_login_button.setStyleSheet("background-color: #4CAF50; color: white;")
        self.admin_login_button = QPushButton("管理员登录")
        self.admin_login_button.setStyleSheet("background-color: #008CBA; color: white;")

        layout = QVBoxLayout()
        layout.addWidget(self.username_label)
        layout.addWidget(self.username_input)
        layout.addWidget(self.password_label)
        layout.addWidget(self.password_input)
        layout.addWidget(self.user_login_button)
        layout.addWidget(self.admin_login_button)

        self.setLayout(layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    login_window = LoginWindow()
    login_window.show()
    sys.exit(app.exec_())
