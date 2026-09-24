from Chapter5.bmi_project.classes.bmi_status import Status
from Chapter5.bmi_project.ui.BMIMainWindow import Ui_MainWindow


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
        self.pushButton.clicked.connect(self.invoke_bmi)

    def invoke_bmi(self):
        height=float(self.lineEdit_Height.text())
        weight=float(self.lineEdit_Weight.text())
        c=Status(height,weight)
        result=c.cal_BMI()
        bmi=result[0]
        status=result[1]
        self.label_BMIResult.setText(str(bmi))
        self.label_StatusResult.setText(str(status))
