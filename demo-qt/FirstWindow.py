from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *

from AddressBookWidget import AddressBookWidget
from FirstWidget import FirstWidget
from SecondWidget import SecondWidget
from WidgetComboBox import WidgetComboBox
from WidgetQridLayout import WidgetGridLayout


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
        #second_widget = SecondWidget(self)
        grid_layout_widget = WidgetGridLayout(self)
        #address_widget = AddressBookWidget(self)

        #combo_box = WidgetComboBox(self)
        self.setCentralWidget(grid_layout_widget)



