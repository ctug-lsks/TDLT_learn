from Chapter5.gpa_project.classes.course import Course
from Chapter5.gpa_project.ui.GPAMainWindow import Ui_MainWindow


class GPAMainWindowEx(Ui_MainWindow):
    def __init__(self):
        pass
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow=MainWindow
        self.setupSignalAndSlot()
    def show_window(self):
        self.MainWindow.show()
    def setupSignalAndSlot(self):
        self.pushButtonGPA.clicked.connect(self.invoke_gpa)

    def invoke_gpa(self):
        ongoing=float(self.lineEditOnGoing.text())
        midterm=float(self.lineEditMidterm.text())
        final=float(self.lineEditFinal.text())
        talent=float(self.lineEditTalent.text())
        percent_ongoing=float(self.lineEditOnGoingPercent.text())/100
        percent_midterm=float(self.lineEditMidtermPercent.text())/100
        percent_final=float(self.lineEditFinalPercent.text())/100
        percent_talent=float(self.lineEditTalentPercent.text())/100
        c=Course(ongoing,percent_ongoing,midterm,percent_midterm, final, percent_final, talent, percent_talent)
        gpa=c.cal_GPA()
        self.labelGPAResult.setText(str(gpa))