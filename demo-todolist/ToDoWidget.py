from PyQt5.QtWidgets import QWidget, QVBoxLayout, QListView, QLineEdit, QPushButton, QHBoxLayout

from ToDoModel import ToDoModel


class ToDoWidget(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.v_layout_box = QVBoxLayout()
        self.list_view = QListView()
        self.edit_todo_text = QLineEdit()
        self.add_button = QPushButton('ajouter')
        self.delete_button = QPushButton('supprimer')
        self.complete_button = QPushButton('valider')
        self.todos = []
        self.todo_model = ToDoModel(self.todos)
        self.createwidget()


    def createwidget(self):
        self.v_layout_box.addWidget(self.list_view)
        h_box_layout = QHBoxLayout()
        h_box_layout.addWidget(self.complete_button)
        h_box_layout.addWidget(self.delete_button)
        self.v_layout_box.addLayout(h_box_layout)
        self.v_layout_box.addWidget(self.edit_todo_text)
        self.v_layout_box.addWidget(self.add_button)
        self.setLayout(self.v_layout_box)

