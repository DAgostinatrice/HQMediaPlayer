from PyQt5.QtCore import Qt
from PyQt5.QtGui import QTextCursor, QFont, QIcon
from PyQt5.QtWidgets import QTextEdit, QWidget

import files


# noinspection PyArgumentList
class EmbeddedConsole(QWidget):
    CONSOLE_STYLESHEET = ("QTextEdit {border-style: solid; border-width: 3px;"
                          "background-color: #000; border-color: #DDD;"
                          "color: #C8C8C8; font-size: 13px; font-family: Consolas;}")

    def __init__(self):
        super(EmbeddedConsole, self).__init__(None)
        self.setMinimumSize(480, 360)
        self.setMaximumSize(480, 360)
        self.setGeometry(50, 50, 480, 360)
        self.setFont(QFont("Consolas", 10))
        self.setWindowTitle("Debug Console")
        self.setWindowIcon(QIcon(files.Images.HQPLAYER_LOGO))

        self.first_write = True

        self.console = QTextEdit(self)
        self.console.setGeometry(0, 0, 480, 360)
        self.console.setStyleSheet(self.CONSOLE_STYLESHEET)
        self.console.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.console.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.console.setReadOnly(True)

    def write(self, text):
        """Add msg to the console's output, on a new line.
           Also writes it to a file.

        :param text: String to output
        """
        if self.first_write:
            with open(files.DEBUG_FILE, 'a') as f:
                f.write("----------\n{0}\n".format(text))
            self.first_write = False
        else:
            with open(files.DEBUG_FILE, 'a') as f:
                f.write("{0}\n".format(text))

        self.console.insertPlainText("{0}\n".format(text))
        self.console.moveCursor(QTextCursor.End)
