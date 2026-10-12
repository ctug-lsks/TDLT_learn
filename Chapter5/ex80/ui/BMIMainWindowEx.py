from PyQt6.QtWidgets import QMessageBox
from fontTools.ttx import process

from Chapter5.ex80.libs.my_module import calc_bmi
from Chapter5.ex80.ui.BMIMainWindow import Ui_MainWindow


class BMIMainWindowEx(Ui_MainWindow):
    def __init__(self):
        pass
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow=MainWindow
        self.setupSignalAndSlot()
    def show_window(self):
        self.MainWindow.show()
    def setupSignalAndSlot(self):
        self.pushButton_process.clicked.connect(self.process_BMI)
        self.pushButton_clear.clicked.connect(self.process_clear)
        self.pushButton_exit.clicked.connect(self.call_close_app)
    def process_BMI(self):
        try:
            h=float(self.heightLineEdit.text())
            w=float(self.weightLineEdit.text())
            # result=calc_bmi(h,w)
            # self.label_BMI_value.setText(str(result[0]))
            # self.label_classification.setText(str(result[1]))
            # self.label__disease.setText(str(result[2]))
            bmi, type, risk=calc_bmi(h,w)
            self.label_BMI_value.setText(str(bmi))
            self.label_classification.setText(str(type))
            self.label__disease.setText(str(risk))
        except ValueError:
            msg = QMessageBox()
            msg.setWindowTitle("Lỗi nhập liệu")
            msg.setText("Nhập sai rồi bà ui. Nhập lại nha")
            msg.setIcon(QMessageBox.Icon.Critical)
            msg.exec()
            self.process_clear()
    def process_clear(self):
        self.heightLineEdit.setText("")
        self.weightLineEdit.setText("")
        self.label_BMI_value.setText("")
        self.label_classification.setText("")
        self.label__disease.setText("")
        self.heightLineEdit.setFocus()
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