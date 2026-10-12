from PyQt6.QtWidgets import QCompleter

from Chapter7.ui.Register.RegisterMainWindow import Ui_MainWindow


class RegisterMainWindowEx(Ui_MainWindow):
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        cities = ["Hà Nội", "Huế", "Đà Nẵng", "Đà Lạt", "Hồ Chí Minh", "Cần Thơ"]
        completer = QCompleter(cities)
        self.cityProvinceLineEdit.setCompleter(completer)
        self.setupSignalandSlot()
    def show(self):
        self.MainWindow.show()
    def setupSignalandSlot(self):
        pass