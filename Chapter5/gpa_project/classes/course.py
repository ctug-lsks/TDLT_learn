class Course:
    def __init__(self, ongoing=0, percent_ongoing=0.225,
                 midterm=0, percent_midterm=0.15,
                 final = 0, percent_final=0.375,
                 talent=0, percent_talent=0.15,):
        self.ongoing = ongoing
        self.percent_ongoing = percent_ongoing
        self.midterm = midterm
        self.percent_midterm = percent_midterm
        self.final = final
        self.percent_final = percent_final
        self.talent = talent
        self.percent_talent = percent_talent

    def cal_GPA(self):
        gpa = (self.ongoing*self.percent_ongoing+
               self.midterm*self.percent_midterm+
               self.final*self.percent_final+
               self.talent*self.percent_talent)
        return gpa