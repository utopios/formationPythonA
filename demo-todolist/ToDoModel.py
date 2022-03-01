from PyQt5 import QtGui
from PyQt5.QtCore import QAbstractListModel, Qt


class ToDoModel(QAbstractListModel):
    def __init__(self, todos=None):
        super(ToDoModel, self).__init__()
        self.todos = todos or []

    def rowCount(self, index):
        return len(self.todos)

    def data(self, index, role):
        if role == Qt.DisplayRole:
            _, content = self.todos[index.row()]
            return content
        if role == Qt.DecorationRole:
            status, _ = self.todos[index.row()]
            if status:
                return QtGui.QImage('done.png')

