import sys

from PyQt6.QtWidgets import QApplication, QMainWindow

from Chapter7.ui.Register.RegisterMainWindowEx import RegisterMainWindowEx

app = QApplication(sys.argv)
myui=RegisterMainWindowEx()
myui.setupUi(QMainWindow())
myui.show()
app.exec()