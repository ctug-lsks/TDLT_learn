from PyQt6.QtWidgets import QApplication, QMainWindow

from Chapter5.ex70.ui.Ex70MainWindowEx import Ex70MainWindowEx

app=QApplication([])
myui=Ex70MainWindowEx()
myui.setupUi(QMainWindow())
myui.show_window()
app.exec()