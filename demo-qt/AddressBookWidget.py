from PyQt5.QtWidgets import QWidget, QGridLayout, QLabel, QTextEdit, QVBoxLayout, QPushButton, QHBoxLayout


class AddressBookWidget(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.grid_layout = QGridLayout()
        self.grid_layout.setRowStretch(0, 1)
        self.grid_layout.setRowStretch(1, 3)
        self.grid_layout.setRowStretch(2, 1)
        self.setLayout(self.grid_layout)
        self.firstrow()
        self.secondrow()
        self.thirdrow()

    def firstrow(self):
        label = QLabel('Name : ')
        self.grid_layout.addWidget(label, 0, 0)
        edit_text_name = QTextEdit()
        self.grid_layout.addWidget(edit_text_name, 0, 1)

    def secondrow(self):
        label = QLabel('Address : ')
        self.grid_layout.addWidget(label, 1, 0)
        edit_text_address = QTextEdit()
        self.grid_layout.addWidget(edit_text_address, 1, 1)
        self.verticalbuttons()

    def thirdrow(self):
        h_layout = QHBoxLayout()
        button_previous = QPushButton('Previous')
        button_previous.setEnabled(False)
        h_layout.addWidget(button_previous)
        button_next = QPushButton('Next')
        button_next.setEnabled(False)
        h_layout.addWidget(button_next)
        self.grid_layout.addLayout(h_layout, 2, 1)


    def verticalbuttons(self):
        layout_vertical = QVBoxLayout()
        button_add = QPushButton('Add')
        button_add.setEnabled(False)
        layout_vertical.addWidget(button_add)
        button_submit = QPushButton('Submit')
        layout_vertical.addWidget(button_submit)
        self.grid_layout.addLayout(layout_vertical, 1, 2)
