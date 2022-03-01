import sys
from unittest import TestCase
from unittest.mock import patch

from PyQt5.QtCore import Qt
from PyQt5.QtTest import QTest
from PyQt5.QtWidgets import QApplication

from ControllerDb import ControllerDb
from HomeWindow import HomeWindow
from ToDoWidget import ToDoWidget


class ToDoWidgetTest(TestCase):


    # test endtoEnd pour le clique d'un bouton
    @patch('ControllerDb.ControllerDb')
    def testaddtodo(self, mock_controller_db):
        # A => Arange
        app = QApplication(sys.argv)
        homewindow = HomeWindow()
        #controller_db = ControllerDb()
        mock_controller_db.add.return_value = False
        todowidget = ToDoWidget(homewindow, mock_controller_db)
        #homewindow.setCentralWidget(todowidget)
        # Act
        todowidget.edit_todo_text.setText('test')
        QTest.mouseClick(todowidget.add_button, Qt.LeftButton)
        # Assert
        self.assertEqual(len(todowidget.todo_model.todos), 1)
