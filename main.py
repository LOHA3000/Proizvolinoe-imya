import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QColor
import random


class MyWidget(QMainWindow):
    def __init__(self):
        self.draw = False
        self.k = 20
        self.coordinates = []
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.setWindowTitle('Git и желтые окружности')

        self.pushButton.clicked.connect(self.run)

    def run(self):
        k = random.randint(10, 100)
        x_pos = random.randint(10, 556)
        y_pos = random.randint(10, 332)
        self.coordinates.append([x_pos, y_pos, k])
        self.update()

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.drawFlag(qp)
        qp.end()

    def drawFlag(self, qp):
        qp.setBrush(QColor(255, 255, 0))
        for i in self.coordinates:
            qp.drawEllipse(i[0], i[1], i[2], i[2])


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
