from PyQt6.QtWidgets import QMessageBox

from Chapter5.ex82.libs.my_module import calc_bill
from Chapter5.ex82.ui.Ex82MainWindow import Ui_MainWindow


class Ex82MainWindowEx(Ui_MainWindow):
    def __init__(self):
        pass
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow=MainWindow
        self.setupSignalAndSlot()
    def show_window(self):
        self.MainWindow.show()
    def setupSignalAndSlot(self):
        self.pushButton_process.clicked.connect(self.process_calc)
        self.pushButton_clear.clicked.connect(self.process_clear)
        self.pushButton_exit.clicked.connect(self.call_close_app)
    def process_calc(self):
        try:
            oldNumberOfKWh = float(self.oldNumberOfKWhLineEdit.text())
            newNumberOfKWh = float(self.newNumberOfKWhLineEdit.text())
            if self.radioButton_withcard.isChecked():
                type=1
            else:
                type=0
            result=calc_bill(type,oldNumberOfKWh,newNumberOfKWh)
            self.label_result.setText(str(result))
        except ValueError:
            msg = QMessageBox()
            msg.setWindowTitle("Lỗi nhập liệu")
            msg.setText("Nhập sai rồi bà ui. Nhập lại nha")
            msg.setIcon(QMessageBox.Icon.Critical)
            msg.exec()
            self.process_clear()
    def process_clear(self):
        self.customerNameLineEdit.setText("")
        self.newNumberOfKWhLineEdit.setText("")
        self.oldNumberOfKWhLineEdit.setText("")
        self.label_result.setText("")
        self.customerNameLineEdit.setFocus()
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