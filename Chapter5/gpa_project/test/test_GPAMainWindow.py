from PyQt6.QtWidgets import QApplication, QMainWindow

from Chapter5.gpa_project.ui.GPAMainWindowEx import GPAMainWindowEx

app = QApplication([])
gpa_ui = GPAMainWindowEx()
gpa_ui.setupUi(QMainWindow())
gpa_ui.show_window()
app.exec()
    