from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QVBoxLayout


class FirstWidget(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        label = QLabel('mon label')
        label.setAlignment(Qt.AlignHCenter)
        #label.setGeometry(10, 10, 200, 20)
        button = QPushButton('Yes')
        #button.setGeometry(10, 50, 200, 40)
        layout = QVBoxLayout()
        layout.addWidget(label)
        layout.addWidget(button)
        self.setLayout(layout)
