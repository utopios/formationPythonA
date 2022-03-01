import sys

from PyQt5.QtWidgets import QApplication
from HomeWindow import HomeWindow

def main():
    app = QApplication(sys.argv)
    w1 = HomeWindow()
    w1.show()
    w1.setWindowTitle('ToDo List')

    app.exec()


if __name__ == '__main__':
    main()

