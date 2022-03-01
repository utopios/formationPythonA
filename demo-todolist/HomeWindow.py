from PyQt5 import uic

from MessageDialog import MessageDialog
from ToDoWidget import ToDoWidget
from PyQt5.QtWidgets import *


# Ui_HomeWindow, QtBaseClass = uic.loadUiType("homewindow.ui")
# class HomeWindow(QMainWindow, Ui_HomeWindow):
class HomeWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        # Ui_HomeWindow.__init__(self)
        # self.setupUi(self)
        todo_widget = ToDoWidget(self)
        dialog_message = MessageDialog(self)
        todo_widget.successAdd.connect(dialog_message.show)
        self.setCentralWidget(todo_widget)
