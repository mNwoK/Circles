from PyQt5 import uic
import sys

from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QMainWindow, QApplication
import random


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        uic.loadUi("main.ui", self)
        self.pushButton.clicked.connect(self.paint)
        self.do_paint = False

    def sharik(self):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            qp.setBrush(QColor(255, 255, 0))
            a = random.randint(0, 100)
            qp.drawEllipse(QPoint(0, 0), a, a)
            qp.end()

    def paint(self):
        self.do_paint = True
        self.repaint()

