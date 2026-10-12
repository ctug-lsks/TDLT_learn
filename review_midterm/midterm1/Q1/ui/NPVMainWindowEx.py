from PyQt6.QtWidgets import QMessageBox

from review_midterm.midterm1.Q1.Q1 import calc_NPV, is_investment
from review_midterm.midterm1.Q1.ui.NPVMainWindow import Ui_MainWindow


class NPVMainWindowEx(Ui_MainWindow):
    def __init__(self):
        pass
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow=MainWindow
        self.setupSignalAndSlot()
    def show_window(self):
        self.MainWindow.show()
    def setupSignalAndSlot(self):
        self.pushButton_calcNPV.clicked.connect(self.process_NPV)
        self.pushButton_clear.clicked.connect(self.clear)
        self.pushButton_exit.clicked.connect(self.process_exit)
    def process_NPV(self):
        c0=float(self.initialInvesmentCostsC0LineEdit.text())
        ct=float(self.netCashFlowAtTimeTLineEdit.text())
        r=float(self.discountRateRLineEdit.text())/100
        t=float(self.projectImplementTimeTLineEdit.text())
        NPV=calc_NPV(c0,ct,r,t)
        self.label_NPV.setText(str(NPV))
        self.label_result.setText(str(is_investment(NPV)))
    def clear(self):
        self.initialInvesmentCostsC0LineEdit.setText("")
        self.netCashFlowAtTimeTLineEdit.setText("")
        self.discountRateRLineEdit.setText("")
        self.projectImplementTimeTLineEdit.setText("")
        self.label_NPV.setText("")
        self.label_result.setText("")
        self.initialInvesmentCostsC0LineEdit.setFocus()
    def process_exit(self):
        msgBox = QMessageBox()
        msgBox.setWindowTitle("Xac nhan thoat")
        msgBox.setText("Bye bye, sureeeeeeeee ?????????")
        msgBox.setIcon(QMessageBox.Icon.Question)
        buttons = QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        msgBox.setStandardButtons(buttons)
        ret = msgBox.exec()
        if ret == QMessageBox.StandardButton.Yes:
            exit(0)
