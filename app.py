import sys
import json
from collections import OrderedDict
import random

from PyQt5.QtWidgets import (
    QApplication, QDialog, QMainWindow, QMessageBox
)

from main_window_ui import Ui_MainWindow

class Window(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.generateButton()
    def about(self):
        QMessageBox.about(
            self,
            "About Sample Editor",
            "<p>A sample text editor app built with:</p>"
            "<p>- PyQt</p>"
            "<p>- Qt Designer</p>"
            "<p>- Python</p>",
        )

    def generatePbClicked(self):
        # let's Call functions!!
        word, meaning = self.generateRandomWord()
        self.wordOutput.setText(word)
        self.meaningOutput.setText(meaning)
    def generateButton(self):
        self.generatePb.clicked.connect(self.generatePbClicked)
    def generateRandomWord(self):
        randomId = str(random.randint(1, 54000))
        with open('wordsDictionary.json') as data_file:
            data = json.load(data_file)
            for key, value in data.items():
                if key == randomId:
                    word = data[key]['Word']
                    meaning = data[key]['Meaning']

        return word, meaning


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec())


