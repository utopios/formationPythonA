from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QWidget, QGridLayout, QLabel, QTextEdit, QVBoxLayout, QPushButton, QHBoxLayout, QListView

from CountryModel import CountryModel


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
        self.countriesrow()
        self.thirdrow()

    def firstrow(self):
        label = QLabel('Name : ')
        self.grid_layout.addWidget(label, 0, 0)
        self.edit_text_name = QTextEdit()
        self.grid_layout.addWidget(self.edit_text_name, 0, 1)

    def secondrow(self):
        label = QLabel('Address : ')
        self.grid_layout.addWidget(label, 1, 0)
        self.edit_text_address = QTextEdit()
        self.grid_layout.addWidget(self.edit_text_address, 1, 1)
        self.verticalbuttons()

    def countriesrow(self):
        label = QLabel('Country : ')
        self.grid_layout.addWidget(label, 2, 0)
        self.list_view = QListView()
        #La création du model à envoyer dans le widget list
        #model = QStandardItemModel(self.list_view)
        countries = ["en", "fr", "be"]
        self.model = CountryModel(countries)

        # for c in countries:
        #     item = QStandardItem(c)
        #     item.setCheckable(True)
        #     model.appendRow(item)

        #model.itemChanged.connect(self.countrychanged)
        self.list_view.setModel(self.model)
        self.grid_layout.addWidget(self.list_view, 2, 1)
        vertical_layout = QVBoxLayout()
        self.edit_text_new_country = QTextEdit()
        vertical_layout.addWidget(self.edit_text_new_country)
        self.button_add_country = QPushButton('ajouter')
        self.button_add_country.clicked.connect(self.addcountry)
        vertical_layout.addWidget(self.button_add_country)
        self.grid_layout.addLayout(vertical_layout, 2, 2)

    def thirdrow(self):
        h_layout = QHBoxLayout()
        button_previous = QPushButton('Previous')
        button_previous.setEnabled(False)
        h_layout.addWidget(button_previous)
        button_next = QPushButton('Next')
        button_next.setEnabled(False)
        h_layout.addWidget(button_next)
        self.grid_layout.addLayout(h_layout, 3, 1)


    def verticalbuttons(self):
        layout_vertical = QVBoxLayout()
        button_add = QPushButton('Add')
        button_add.setEnabled(False)
        layout_vertical.addWidget(button_add)
        self.button_submit = QPushButton('Submit')
        layout_vertical.addWidget(self.button_submit)
        self.button_submit.clicked.connect(self.addaddress)
        self.grid_layout.addLayout(layout_vertical, 1, 2)




    def addaddress(self):
        files = open('data/data.txt', 'a')
        files.write(f"Name : {self.edit_text_name.toPlainText()}, address : {self.edit_text_address.toPlainText()}")
        files.close()

    def countrychanged(self, item):

        self.edit_text_name.setText(item)

    def keyPressEvent(self, a0) -> None:
        self.edit_text_name.setText(a0.key())

    def mousePressEvent(self, a0) -> None:
        self.edit_text_address.setText(str(a0.globalPos().x()))

    def addcountry(self):
        text = self.edit_text_new_country.toPlainText()
        if text:
            self.model.countries.append(text)
            self.model.layoutChanged.emit()



