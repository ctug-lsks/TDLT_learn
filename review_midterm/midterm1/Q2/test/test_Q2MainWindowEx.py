from PyQt6.QtWidgets import QApplication, QMainWindow

from review_midterm.midterm1.Q2.ui.Q2MainWindowEx import Q2MainWindowEx

app = QApplication([])
myui = Q2MainWindowEx()
myui.setupUi(QMainWindow())
myui.show_window()
app.exec()