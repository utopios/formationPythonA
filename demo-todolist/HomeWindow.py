from ToDoWidget import ToDoWidget
from PyQt5.QtWidgets import *


class HomeWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        todo_widget = ToDoWidget(self)
        self.setCentralWidget(todo_widget)
