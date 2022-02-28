from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QComboBox


class WidgetComboBox(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.layout = QVBoxLayout()
        self.label = QLabel()
        self.combo = QComboBox()
        self.combo.addItems(["Alice", "Bob", "Carl"])
        self.combo.currentTextChanged.connect(self.updatename)
        self.layout.addWidget(self.combo)
        self.layout.addWidget(self.label)
        self.setLayout(self.layout)

    def updatename(self, name):
        self.label.setText(name)