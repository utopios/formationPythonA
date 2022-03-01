from PyQt5.QtWidgets import QDialog


class MessageDialog(QDialog):
    def __init__(self, parent):
        super(MessageDialog, self).__init__(parent)