from PyQt6.QtWidgets import QMainWindow, QMessageBox

from Chapter7.ui.Login.LoginMainWindow import Ui_MainWindow
from Chapter7.ui.MainSystemMainWindowEx import MainSystemMainWindowEx


class LoginMainWindowEx(Ui_MainWindow):
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow=MainWindow
        self.setupSignalandSlot()
    def show(self):
        self.MainWindow.show()
    def setupSignalandSlot(self):
        self.pushButton_login.clicked.connect(self.process_login)
    def process_login(self):
        username=self.lineEdit_username.text()
        password=self.lineEdit_password.text()
        if username=="VCT" and password=="123":
            self.mysui=MainSystemMainWindowEx()
            self.mysui.setupUi(QMainWindow())
            self.mysui.show()
            self.MainWindow.close()
        else:
            self.msg=QMessageBox()
            self.msg.setText("Login Failed")
            self.msg.show()

