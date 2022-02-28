from PyQt5.QtWidgets import QWidget, QHBoxLayout, QLabel, QTextEdit, QVBoxLayout


class SecondWidget(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        layoutHFirstName = QHBoxLayout()
        layoutHFirstName.addWidget(QLabel('Prénom : '))
        layoutHFirstName.addWidget(QTextEdit())
        layoutHLastName = QHBoxLayout()
        layoutHLastName.addWidget(QLabel('Nom : '))
        layoutHLastName.addWidget(QTextEdit())
        verticalLayout = QVBoxLayout()
        verticalLayout.addLayout(layoutHLastName)
        verticalLayout.addLayout(layoutHFirstName)
        self.setLayout(verticalLayout)
