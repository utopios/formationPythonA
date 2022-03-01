from ctypes import *


class ControllerDb:
    def __init__(self):
        self.connection_string = None

    def add(self, todo):
        # Logique metier qui communique avec une Api rest
        # Appeler une fonction dans une librairie en c qui permet d'erire le contenu de la todo dans un fichier.
        _, content = todo
        c_data_writer = CDLL('./../projetc/lib1.so')
        result = c_data_writer.write_in_file(c_char_p(content.encode('utf-8')))
        return result == 1
