def calc_bmi(h,w):
    bmi=round((w/(h*h)),2)
    if bmi<18.5:
        type="Thin"
        risk="Low"
    elif 18.5<=bmi<25:
        type="Normal"
        risk="Normal"
    elif 25<=bmi<30:
        type="Slightly Fat"
        risk="High"
    elif 30<=bmi<35:
        type="Obesity Level 1"
        risk="High"
    elif 35<=bmi<40:
        type="Obesity Level 2"
        risk="Very High"
    else:
        type="Obesity Level 3"
        risk="Danger"
    return bmi, type,risk