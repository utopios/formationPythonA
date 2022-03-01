from PyQt5.QtCore import QAbstractListModel, Qt


class CountryModel(QAbstractListModel):
    def __init__(self, countries=None):
        super(CountryModel, self).__init__()
        self.countries = countries or []

    # la méthode qui permet d'afficher chaque element
    def data(self, index, role):
        if role == Qt.DisplayRole:
            text = self.countries[index.row()]
            return text

    #Methode utilisée par la listview pour avoir le nombre d'elements à afficher
    def rowCount(self, index):
        return len(self.countries)
