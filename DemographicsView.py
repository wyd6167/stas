import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QAbstractItemDelegate, QApplication, QGraphicsPixmapItem, QGraphicsScale, QGraphicsScene, \
    QGraphicsView, QMainWindow
from PyQt5.QtCore import *
import cv2


class Ui_Form(QMainWindow):
    def __init__(self):
        super(Ui_Form, self).__init__()
        self.setObjectName("try")
        rect = QApplication.instance().desktop().availableGeometry(self)
        self.resize(int(rect.width() * 2 / 3), int(rect.height() * 2 / 3))
        self.initUI()
        self._zoom = 0
        self._empty = True
        self.cur_img = None
        self.src_img = None
        self._photo = QGraphicsPixmapItem()  # 预设场景的图元，也就是显示的图片

    def initUI(self):
        self.graphicsView = QtWidgets.QGraphicsView(self)
        self.graphicsView.setGeometry(QtCore.QRect(40, 50, 600, 600))
        self.graphicsView.setObjectName("graphicsView")
        self.graphicsView.setDragMode(QGraphicsView.ScrollHandDrag)
        self.graphicsView.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)  # 隐藏滑动条
        self.graphicsView.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)  # 隐藏滑动条
        self.graphicsView.setMinimumSize(640, 480)  # 设置窗体的最小值
        self.graphicsView.setRenderHints(QPainter.Antialiasing | QPainter.HighQualityAntialiasing |
                                         QPainter.SmoothPixmapTransform)
        self.graphicsView.setViewportUpdateMode(self.graphicsView.SmartViewportUpdate)

        # self.setCentralWidget(self.graphicsView)     #对graphicsView进行影响

        self.scene = QGraphicsScene(self)
        self.graphicsView.setScene(self.scene)
        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setGeometry(QtCore.QRect(700, 0, 93, 28))
        self.pushButton.clicked.connect(self.on_pushButton_clicked)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setText('插入图片')

        self.graphicsView.setAlignment(Qt.AlignCenter)
        self.graphicsView.setDragMode(QGraphicsView.ScrollHandDrag)  # 设置的拖拽手标以及允许拖拽
        self.graphicsView.setAcceptDrops(False)
        self._delta = 0.1  # 缩放

    def on_pushButton_clicked(self):
        self.path = QtWidgets.QFileDialog.getOpenFileName(self, "openImage", " ",
                                                          "*.jpg;;*.png;;All Files(*)")  # 获取本地文件路径
        pixmap = QPixmap(self.path[0])
        self.cur_img = cv2.imread(self.path[0])
        QGraphicsPixmapItem.ItemIsMovable

        self._photo = QGraphicsPixmapItem(pixmap)  # 将QPixmap对象转换成为图元

        self._photo.setFlags(QGraphicsPixmapItem.ItemIsFocusable)

        self.scene.addItem(self._photo)
        self.update_image(self.cur_img)
        self.graphicsView.fitInView(QGraphicsPixmapItem(QPixmap(pixmap)))  # 图片自适应铺满窗口

    def update_image(self, img):
        self._empty = False
        self._photo.setPixmap(self.img_to_pixmap(img))

    def img_to_pixmap(self, img):
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # bgr -> rgb
        h, w, c = img.shape  # 获取图片形状
        image = QImage(img, w, h, 3 * w, QImage.Format_RGB888)  # 获取QImage图像
        return QPixmap.fromImage(image)
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    Ui = Ui_Form()
    Ui.show()
    sys.exit(app.exec_())