from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton, QLabel


class WidgetGridLayout(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.grid_layout = QGridLayout()
        self.makeButton()
        self.specialButton()
        self.setLayout(self.grid_layout)

    def makeButton(self):
        for x in range(3):
            for y in range(3):
                b = QPushButton(str(str(3*x + y)))
                b.clicked.connect(lambda: self.clickbutton(b))
                self.grid_layout.addWidget(b, x, y)

    def specialButton(self):
        button = QPushButton('special')
        self.grid_layout.addWidget(button, 3, 0, 1, 3)
        self.label = QLabel()
        self.grid_layout.addWidget(self.label, 4, 0, 1, 3)

    def clickbutton(self, button):
        self.label.setText(button.text())

