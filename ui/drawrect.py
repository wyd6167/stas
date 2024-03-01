import sys

from PyQt5.QtCore import QRectF, Qt, QPointF
from PyQt5 import  QtCore
from PyQt5.QtGui import QPainterPath, QPainter, QPen, QBrush
from PyQt5.QtWidgets import QGraphicsRectItem, QApplication, QGraphicsView, QGraphicsScene, QGraphicsItem

def getRectFromLine(pt1, pt2):
    x1, y1 = pt1.x(), pt1.y()
    x2, y2 = pt2.x(), pt2.y()
    return QRectF(x1, y1, abs(x2 - x1), abs(y2 - y1))


def getAccurateRect(point1, point2):
    """
    Always return a rectangle decided by topLeft and its diagonal point
    :param point1: point1
    :param point2: the point1's diagonal point
    :return: a rectangle constructed by point1 and point2
    """
    x1, y1 = point1.x(), point1.y()
    x2, y2 = point2.x(), point2.y()
    rect = None
    if x1 < x2 and y1 < y2:
        rect = getRectFromLine(point1, point2)
    elif x1 > x2 and y1 < y2:
        rect = getRectFromLine(QPointF(x2, y1), QPointF(x1, y2))
    elif x1 < x2 and y1 > y2:
        rect = getRectFromLine(QPointF(x1, y2), QPointF(x2, y1))
    elif x1 > x2 and y1 > y2:
        rect = getRectFromLine(QPointF(x2, y2), QPointF(x1, y1))
    return rect


def getRectOfCircle(center: QPointF, radius: float):
    """
    获取圆的外接矩形
    :param center: 圆形
    :param radius: 半径
    :return:外接矩形
    """
    leftTopX = center.x() - radius
    lefttTopY = center.y() - radius
    rect = QRectF(leftTopX, lefttTopY, 2*radius, 2*radius)
    return rect


class InteractiveGraphicsRectItem(QGraphicsRectItem):
    handleTopLeft = 1
    handleTopRight = 2
    handleBottomLeft = 3
    handleBottomRight = 4
    def __init__(self,
                    rect,
                    radius=5,
                    *args,
                    **kwargs):
        super(InteractiveGraphicsRectItem, self).__init__(*args, **kwargs)
        self.radius = radius
        self.setRect(rect)
        self.setFlag(QGraphicsItem.ItemIsMovable, True)
        self.setFlag(QGraphicsItem.ItemIsSelectable, True)

        points = [rect.topLeft(), rect.topRight(), rect.bottomRight(), rect.bottomLeft()]
        self.circlePath = QPainterPath()
        self.rectPath = QPainterPath()
        self.rectPath.addRect(self.rect())
        for p in points:
            self.circlePath.addEllipse(p,  self.radius,  self.radius)

        self.handleSelected = None  # 用于指示是否选中某个顶点

        self.circleOfFourPoints = []
        for p in points:
            self.circleOfFourPoints.append(getRectOfCircle(p,  self.radius))
        self.pointPosition = {}  # point: 矩形的四个顶点对应的圆的外接矩形
        self.pointPosition[self.handleTopLeft] = self.circleOfFourPoints[0]
        self.pointPosition[self.handleTopRight] = self.circleOfFourPoints[1]
        self.pointPosition[self.handleBottomRight] = self.circleOfFourPoints[2]
        self.pointPosition[self.handleBottomLeft] = self.circleOfFourPoints[3]

    def paint(self, painter: QPainter, item, widget=None):
        # 画矩形， 我们画一个绿色的矩形吧
        # painter.save()  # 保存画笔的属性，
        # painter.setPen(QPen(Qt.green))
        pen = QPen(Qt.red, 2, Qt.SolidLine)
        painter.setPen(pen)
        # 画矩形，当然你也可以不使用QPainterPath，而是直接painter.drawRect(self.rect())
        painter.drawPath(self.rectPath)
        painter.restore()  # 恢复画笔的属性，

        # 画矩形四个顶点上的圆形
        # painter.save()
        # painter.setPen(QPen(Qt.NoPen))  # 不需要边框
        # painter.setBrush(QBrush(Qt.darkBlue))  # 设置填充色为暗蓝色
        # painter.setOpacity(0.5)  # 设置透明度
        # painter.drawPath(self.circlePath)
        #
        # painter.restore()
        super(InteractiveGraphicsRectItem, self).paint(painter, item, widget)


    def handleCursor(self, pos: QPointF):

        for k, circle in self.pointPosition.items():
            if circle.contains(pos):
                return k
        return None

    def mousePressEvent(self, event) -> None:
        if event.buttons() == QtCore.Qt.LeftButton:
            pos = event.pos()
            self.handleSelected = self.handleCursor(pos)
            if self.handleSelected:
                self.mousePressedPos = pos #deepcopy(pos)
            self.update()
        # elif event.buttons() == QtCore.Qt.RightButton:
        #     # self.scene().removeItem(self)
        #     items = self.scene().items(event.scenePos())
        #     self.scene().removeItem(items[0])

    # def mouseReleaseEvent(self, event: 'QGraphicsSceneMouseEvent'):
    #     self.update()

    def mouseMoveEvent(self, event) -> None:
        # print(self.debuginfo() + f"scene pos: {self.scenePos()}")
        # print(self.debuginfo() + f"pos: {self.pos()}")
        # print(self.debuginfo() + f"item's parent is: {self.parentItem()}")
        if self.handleSelected is not None:
            self.interactResize(event.pos())
        else:
            super(InteractiveGraphicsRectItem, self).mouseMoveEvent(event)
        self.update()

    def interactResize(self, mousePos: QPointF):
        """
        Change the geometry acrroding to mouse oerpation.
        :param mousePos: the position of current moving mouse.
        :return: None
        """
        rect = self.rect()
        # print(f"diff = {mousePos - self.mousePressedPos}")
        self.prepareGeometryChange()

        newRect = None
        if self.handleSelected == self.handleTopLeft:
            newRect = getAccurateRect(mousePos, rect.bottomRight())

        elif self.handleSelected == self.handleTopRight:
            newRect = getAccurateRect(mousePos, rect.bottomLeft())
            # self.setRect(newRect)
        elif self.handleSelected == self.handleBottomRight:
            newRect = getAccurateRect(mousePos, rect.topLeft())
            # self.setRect(newRect)

        elif self.handleSelected == self.handleBottomLeft:
            newRect = getAccurateRect(mousePos, rect.topRight())
            # self.setRect(newRect)

        if newRect is not None:
            self.setRect(newRect)
        self.update()
        self.updateData()

    def updateData(self):
        self.rectPath.clear()
        self.circlePath.clear()
        self.circleOfFourPoints.clear()

        rect = self.rect()
        self.rectPath.addRect(rect)

        points = [rect.topLeft(), rect.topRight(), rect.bottomRight(), rect.bottomLeft()]

        for p in points:
            self.circlePath.addEllipse(p, self.radius, self.radius)


        for p in points:
            self.circleOfFourPoints.append(getRectOfCircle(p, self.radius))

        self.pointPosition[self.handleTopLeft] = self.circleOfFourPoints[0]
        self.pointPosition[self.handleTopRight] = self.circleOfFourPoints[1]
        self.pointPosition[self.handleBottomRight] = self.circleOfFourPoints[2]
        self.pointPosition[self.handleBottomLeft] = self.circleOfFourPoints[3]

if __name__ == "__main__":
    app = QApplication(sys.argv)
    view = QGraphicsView()
    scene = QGraphicsScene()
    view.setScene(scene)
    view.setGeometry(0, 0, 1500, 500)
    scene.setSceneRect(0, 0, 1500, 500)
    rect = QRectF(1011, 10, 100, 50)
    rectItem = InteractiveGraphicsRectItem(rect=rect, radius=5)
    scene.addItem(rectItem)

    scene.clear()
    view.show()
    rect = QRectF(10, 10, 100, 50)
    rectItem = InteractiveGraphicsRectItem(rect=rect, radius=5)
    scene.addItem(rectItem)

    # rect1 = QRectF(200, 200, 100, 50)
    # rectItem1 = InteractiveGraphicsRectItem(rect=rect1, radius=5)
    # scene.addItem(rectItem1)

    # view.resize(800, 600)
    view.setWindowTitle(view.tr("interactive rect item"))


    sys.exit(app.exec())