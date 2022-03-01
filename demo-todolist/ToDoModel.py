from PyQt5.QtCore import QAbstractListModel, Qt


class ToDoModel(QAbstractListModel):
    def __init__(self, todos=None):
        super(ToDoModel, self).__init__()
        self.todos = todos or []

    def rowCount(self, index):
        return len(self.todos)

    def data(self, index, role):
        if role == Qt.DisplayRole:
            status, content = self.todos[index.row()]
            return str(status) + content
