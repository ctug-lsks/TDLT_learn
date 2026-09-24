from Chapter5.ex70.libs.my_module import get_number_of_days
from Chapter5.ex70.ui.Ex70MainWindow import Ui_MainWindow


class Ex70MainWindowEx(Ui_MainWindow):
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow=MainWindow #chỗ này là kiểu khai báo ô nhớ có đứa dùng -> cấp phát ô nhớ k dùng --> thu hồi ô nhớ
        self.setupSignalAndSlot()
    def show_window(self):
        self.MainWindow.show()
    def setupSignalAndSlot(self):
        self.pushButton_count.clicked.connect(self.count_days)
    def count_days(self):
        year=int(self.yearLineEdit.text())
        month=int(self.monthLineEdit.text())
        day=get_number_of_days(year,month)
        self.resultfinal_Label.setText(str(day))