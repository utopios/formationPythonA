from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QVBoxLayout


class FirstWidget(QWidget):

    compteur = 0

    def __init__(self, parent):
        super().__init__(parent)
        self.label = QLabel('mon label')
        self.label.setAlignment(Qt.AlignHCenter)
        #label.setGeometry(10, 10, 200, 20)
        button = QPushButton('Yes')
        #button.setGeometry(10, 50, 200, 40)
        button.clicked.connect(self.clickbutton)
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(button)
        self.setLayout(layout)

    def clickbutton(self):
        self.compteur = self.compteur + 1
        self.label.setText(str(self.compteur))
