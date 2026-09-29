from PyQt6.QtWidgets import QApplication, QMainWindow

from Chapter5.ex77.ui.Ex77MainWindowEx import Ex77MainWindowEx

app=QApplication([])
myui=Ex77MainWindowEx()
myui.setupUi(QMainWindow())
myui.show_window()
app.exec()