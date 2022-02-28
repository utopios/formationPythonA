from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QLabel, QPushButton


class FirstWidget(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        label = QLabel('mon label', self)
        label.setAlignment(Qt.AlignHCenter)
        label.setGeometry(10, 10, 200, 20)
        button = QPushButton('Yes', self)
        button.setGeometry(10, 50, 200, 40)
