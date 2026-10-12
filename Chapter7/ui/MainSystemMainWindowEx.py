from PyQt6.QtWidgets import QMessageBox

from Chapter7.ui.MainSystemMainWindow import Ui_MainWindow


class MainSystemMainWindowEx(Ui_MainWindow):
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow=MainWindow
        self.setupSignalandSlot()
    def show(self):
        self.MainWindow.show()
    def setupSignalandSlot(self):
        self.actionExit.triggered.connect(self.process_exit)
    def process_exit(self):
        msgBox = QMessageBox()
        msgBox.setWindowTitle("Xác nhận thoát")
        msgBox.setText("Bye bye, sureeeeeeeee ?????????")
        msgBox.setIcon(QMessageBox.Icon.Question)
        buttons = QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        msgBox.setStandardButtons(buttons)
        ret = msgBox.exec()
        if ret == QMessageBox.StandardButton.Yes:
            exit(0)
