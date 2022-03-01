from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QListView, QLineEdit, QPushButton, QHBoxLayout

from MessageDialog import MessageDialog
from ToDoModel import ToDoModel


class ToDoWidget(QWidget):

    successAdd = pyqtSignal()

    def __init__(self, parent, controller_db=None):
        super().__init__(parent)
        self.v_layout_box = QVBoxLayout()
        self.list_view = QListView()
        self.edit_todo_text = QLineEdit()
        self.add_button = QPushButton('ajouter')
        self.delete_button = QPushButton('supprimer')
        self.complete_button = QPushButton('valider')
        self.todos = []
        self.todo_model = ToDoModel(self.todos)
        self.list_view.setModel(self.todo_model)
        self.createwidget()
        self.connectslot()
        self.controller_db = controller_db


    def createwidget(self):
        self.v_layout_box.addWidget(self.list_view)
        h_box_layout = QHBoxLayout()
        h_box_layout.addWidget(self.complete_button)
        h_box_layout.addWidget(self.delete_button)
        self.v_layout_box.addLayout(h_box_layout)
        self.v_layout_box.addWidget(self.edit_todo_text)
        self.v_layout_box.addWidget(self.add_button)
        self.setLayout(self.v_layout_box)

    def connectslot(self):
        self.add_button.clicked.connect(self.add)
        self.delete_button.clicked.connect(self.delete)
        self.complete_button.clicked.connect(self.complete)


    def add(self):
        content = self.edit_todo_text.text()
        if content:
            todo = (False, content)
            self.todo_model.todos.append(todo)
            self.todo_model.layoutChanged.emit()
            if self.controller_db:
                result = self.controller_db.add(todo)
            self.successAdd.emit()
            self.edit_todo_text.setText("")

    def delete(self):
        indexes = self.list_view.selectedIndexes()
        if indexes:
            index = indexes[0]
            del self.todo_model.todos[index.row()]
            self.todo_model.layoutChanged.emit()
            self.list_view.clearSelection()

    def complete(self):
        indexes = self.list_view.selectedIndexes()
        if indexes:
            index = indexes[0]
            key = index.row()
            status, content = self.todo_model.todos[key]
            self.todo_model.todos[key] = (True, content)
            #self.todo_model.layoutChanged.emit()
            self.todo_model.dataChanged.emit(index, index)
            self.list_view.clearSelection()


