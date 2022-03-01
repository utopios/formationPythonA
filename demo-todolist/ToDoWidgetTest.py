import sys
from unittest import TestCase

from PyQt5.QtCore import Qt
from PyQt5.QtTest import QTest
from PyQt5.QtWidgets import QApplication

from HomeWindow import HomeWindow
from ToDoWidget import ToDoWidget


class ToDoWidgetTest(TestCase):


    # test endtoEnd pour le clique d'un bouton
    def testaddtodo(self):
        # A => Arange
        app = QApplication(sys.argv)
        homewindow = HomeWindow()
        todowidget = ToDoWidget(homewindow)
        #homewindow.setCentralWidget(todowidget)
        # Act
        todowidget.edit_todo_text.setText('test')
        QTest.mouseClick(todowidget.add_button, Qt.LeftButton)
        # Assert
        self.assertEqual(len(todowidget.todo_model.todos), 1)
