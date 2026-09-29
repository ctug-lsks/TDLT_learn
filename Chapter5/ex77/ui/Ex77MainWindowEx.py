from PyQt6.QtWidgets import QMessageBox

from Chapter5.ex77.libs.my_module import cal_operations, do_math
from Chapter5.ex77.ui.Ex77MainWindow import Ui_MainWindow


class Ex77MainWindowEx(Ui_MainWindow):
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow=MainWindow #chỗ này là kiểu khai báo ô nhớ có đứa dùng -> cấp phát ô nhớ k dùng --> thu hồi ô nhớ
        self.setupSignalAndSlot()
    def show_window(self):
        self.MainWindow.show()
    def setupSignalAndSlot(self):
        # self.pushButton_calculate.clicked.connect(self.calculate)
        self.pushButton_calculate.clicked.connect(self.call_math_operation)
        self.pushButton_exit.clicked.connect(self.call_close_app)
    # def calculate(self):
    #     a=float(self.lineEdit_a.text())
    #     b=float(self.lineEdit_b.text())
    #     if self.radioButton_cong.isChecked():
    #         button = "+"
    #     elif self.radioButton_tru.isChecked():
    #         button = "-"
    #     elif self.radioButton_multiple.isChecked():
    #         button = "*"
    #     elif self.radioButton_divide.isChecked():
    #         button = "/"
    #     kq=cal_operations(a,b,button)
    #     self.label_4.setText(str(kq))
    def call_math_operation(self):
        a=float(self.lineEdit_a.text())
        b=float(self.lineEdit_b.text())
        if self.radioButton_cong.isChecked():
            op = "+"
        elif self.radioButton_tru.isChecked():
            op = "-"
        elif self.radioButton_multiple.isChecked():
            op = "*"
        elif self.radioButton_divide.isChecked():
            op = "/"
        # else:
        #     op=""
        kq=do_math(a,b,op)
        self.label_4.setText(str(kq))

    def call_close_app(self):
        msgBox = QMessageBox()
        msgBox.setWindowTitle("Xac nhan thoat")
        msgBox.setText("Bye bye, sureeeeeeeee ?????????")
        msgBox.setIcon(QMessageBox.Icon.Question)
        buttons = QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        msgBox.setStandardButtons(buttons)
        ret = msgBox.exec()
        if ret == QMessageBox.StandardButton.Yes:
            exit(0)



