from PyQt6.QtWidgets import QApplication, QMainWindow
from Chapter5.ex82.ui.Ex82MainWindowEx import Ex82MainWindowEx

app = QApplication([])
myui = Ex82MainWindowEx()
myui.setupUi(QMainWindow())
myui.show_window()
app.exec()