import sys

from PyQt6.QtWidgets import QApplication, QMainWindow

from Chapter7.ui.MainSystemMainWindowEx import MainSystemMainWindowEx

app=QApplication(sys.argv)
mysystem=MainSystemMainWindowEx()
mysystem.setupUi(QMainWindow())
mysystem.show()
app.exec()