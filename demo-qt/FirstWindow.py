from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *

from FirstWidget import FirstWidget
from SecondWidget import SecondWidget


class FirstWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # label = QLabel('first label', self)
        # label.setAlignment(Qt.AlignHCenter)
        # button = QPushButton('first button', self)
        # button.setGeometry(10, 10, 100, 20)
        # dateEdit = QDateEdit(self)
        #self.setCentralWidget

        #first_widget = FirstWidget(self)
        second_widget = SecondWidget(self)
        self.setCentralWidget(second_widget)


