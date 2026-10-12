import sys

from PyQt6.QtWidgets import QApplication, QMainWindow

from Chapter7.ui.LoginMainWindowEx import LoginMainWindowEx

app=QApplication(sys.argv)
myui=LoginMainWindowEx()
myui.setupUi(QMainWindow())
myui.show()
app.exec()