from PyQt6.QtWidgets import QMessageBox

from review_midterm.midterm1.Q2.libs.Q2 import calc_order, reset_order
from review_midterm.midterm1.Q2.ui.Q2MainWindow import Ui_MainWindow


class Q2MainWindowEx(Ui_MainWindow):
    def __init__(self):
        pass
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow=MainWindow
        self.setupSignalAndSlot()
    def show_window(self):
        self.MainWindow.show()
    def setupSignalAndSlot(self):
        self.pushButton_order.clicked.connect(self.process_order)
        self.pushButton_new.clicked.connect(self.process_new)
        self.pushButton_exit.clicked.connect(self.process_exit)
        self.pushButton_reset.clicked.connect(self.process_reset)
    def process_order(self):
        num_dl=float(self.spinBox_Dalat.text())
        num_sp=float(self.spinBox_Sapa.text())
        if num_dl == 0 and num_sp == 0:
            return
        num_sold_dl,num_sold_sp,dl, sp, total = calc_order(num_dl,num_sp)
        self.label_number_sold_Dalat_flowers.setText(str(num_sold_dl))
        self.label_number_sold_Sapa_flowers.setText(str(num_sold_sp))
        self.label_totalrevenueofDalatflowers.setText(str(round(dl,2)))
        self.label_totalrevenueofSapaflowers.setText(str(round(sp,2)))
        self.label_totalrevenue.setText(str(round(total,2)))
    def process_new(self):
        self.spinBox_Sapa.setValue(0)
        self.spinBox_Dalat.setValue(0)
        self.spinBox_Dalat.setFocus()
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
    def process_reset(self):
        reset_order()
        self.spinBox_Dalat.setValue(0)
        self.spinBox_Sapa.setValue(0)
        self.spinBox_Dalat.setFocus()
        self.label_totalrevenueofDalatflowers.setText("")
        self.label_totalrevenueofSapaflowers.setText("")
        self.label_totalrevenue.setText("")
        self.label_number_sold_Dalat_flowers.setText("")
        self.label_number_sold_Sapa_flowers.setText("")

