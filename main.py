import sys
import random
from PyQt6.QtGui import QPainter, QBrush, QColor
from PyQt6.QtWidgets import QWidget, QApplication
from ui import Ui_Form


class DrawCircles(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.paint)
        self.circles = []

    def paint(self):
        circle_radius = random.randint(20, 50)
        x = random.randint(0, self.width() - circle_radius * 2)
        y = random.randint(0, self.height() - circle_radius * 2)
        random_color = QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.circles.append((x, y, circle_radius, random_color))
        self.update()

    def paintEvent(self, event):
        qp = QPainter(self)
        qp.begin(self)
        for x, y, radius, color in self.circles:
            qp.setBrush(QBrush(color))
            qp.drawEllipse(x, y, radius * 2, radius * 2)
        qp.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = DrawCircles()
    ex.show()
    sys.exit(app.exec())
