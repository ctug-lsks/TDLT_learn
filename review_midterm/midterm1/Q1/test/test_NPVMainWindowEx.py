from PyQt6.QtWidgets import QApplication, QMainWindow

from review_midterm.midterm1.Q1.ui.NPVMainWindowEx import NPVMainWindowEx

app = QApplication([])
myui = NPVMainWindowEx()
myui.setupUi(QMainWindow())
myui.show_window()
app.exec()