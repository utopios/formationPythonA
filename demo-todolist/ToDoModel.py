from PyQt5.QtCore import QAbstractListModel


class ToDoModel(QAbstractListModel):
    def __init__(self, todos=None):
        super(ToDoModel, self).__init__()
        self.todos = todos or []