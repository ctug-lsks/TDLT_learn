from PyQt6.QtWidgets import QApplication, QMainWindow

from Chapter5.bmi_project.ui.BMIMainWindowEx import BMIMainWindowEx

app = QApplication([])
gpa_ui = BMIMainWindowEx()
gpa_ui.setupUi(QMainWindow())
gpa_ui.show_window()
app.exec()