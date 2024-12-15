import sys
import random
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPainter, QBrush
from PyQt6.QtWidgets import QWidget, QApplication
from PyQt6 import uic


class DrawCircles(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.pushButton.clicked.connect(self.paint)
        self.circles = []
    def paint(self):
        circle_radius = random.randint(20, 50)
        x = random.randint(0, self.width() - circle_radius * 2)
        y = random.randint(0, self.height() - circle_radius * 2)
        self.circles.append((x, y, circle_radius))
        self.update()

    def paintEvent(self, event):
        qp = QPainter(self)
        qp.begin(self)
        qp.setBrush(QBrush(Qt.GlobalColor.yellow))
        for x, y, radius in self.circles:
            qp.drawEllipse(x, y, radius * 2, radius * 2)
        qp.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = DrawCircles()
    ex.show()
    sys.exit(app.exec())
