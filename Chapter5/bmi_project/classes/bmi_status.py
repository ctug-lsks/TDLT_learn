from tensorflow.python.framework.test_ops import none


class Status:
    def __init__(self, height=None, weight=None):
        self.height = height
        self.weight = weight

    def cal_BMI(self):
        bmi=round((self.weight/(self.height*self.height)),2)
        if bmi<18.5:
            status="thin"
        elif bmi<24.9:
            status="normal"
        elif bmi<29.9:
            status="fat"
        else:
            status="obesity"

        return bmi, status