import sys

from PyQt5.QtWidgets import *

from FirstWindow import FirstWindow


def start_app():
    app = QApplication(sys.argv)
    w1 = FirstWindow()
    w1.show()
    app.exec()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
   start_app()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
