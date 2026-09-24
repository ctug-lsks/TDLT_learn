from PyQt6.QtWidgets import QApplication, QMainWindow

from Chapter5.ex73.ui.Ex73MainWindowEx import Ex73MainWindowEx

app=QApplication([])
myui=Ex73MainWindowEx()
myui.setupUi(QMainWindow())
myui.show_window()
app.exec()