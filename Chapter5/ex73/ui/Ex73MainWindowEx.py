from unittest import result

from Chapter5.ex73.libs.my_module import giai_pt_bac2
from Chapter5.ex73.ui.Ex73MainWindow import Ui_MainWindow


class Ex73MainWindowEx(Ui_MainWindow):
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow=MainWindow #chỗ này là kiểu khai báo ô nhớ có đứa dùng -> cấp phát ô nhớ k dùng --> thu hồi ô nhớ
        self.setupSignalAndSlot()
    def show_window(self):
        self.MainWindow.show()
    def setupSignalAndSlot(self):
        self.pushButton_count.clicked.connect(self.count)
    def count(self):
        hsa=float(self.hsaLineEdit.text())
        hsb=float(self.hsbLineEdit.text())
        hsc=float(self.hscLineEdit.text())
        kq=giai_pt_bac2(hsa,hsb,hsc)
        self.resultfinal_Label.setText(str(kq))
