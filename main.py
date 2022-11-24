import random
import sys

from PyQt5 import uic
from PyQt5.QtCore import QPoint
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QMainWindow, QApplication


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        uic.loadUi("Ui.ui", self)
        self.pushButton.clicked.connect(self.paint)
        self.do_paint = False

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.sharik(qp)
            qp.end()

    def sharik(self, qp):
        if self.do_paint:
            qp.setBrush(QColor(255, 255, 0))
            a = random.randint(0, 200)
            qp.drawEllipse(QPoint(400, 300), a, a)

    def paint(self):
        self.do_paint = True
        self.repaint()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec())
