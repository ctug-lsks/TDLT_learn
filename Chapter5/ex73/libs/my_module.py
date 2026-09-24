from math import sqrt


def giai_pt_bac2(hsa, hsb, hsc):
    a=float(hsa)
    b=float(hsb)
    c=float(hsc)
    if a == 0:
        # bx+c=0
        if b == 0 and c == 0:
            return "Infinite solutions"
        elif b == 0 and c != 0:
            return "No solutions"
        else:
            x = round((-c / b),2)
            return f"Solution x={x}"
    else:
        delta = b ** 2 - 4 * a * c
        if delta < 0:
            return "No solutions"
        elif delta == 0:
            x = round((-b / (2 * a)),2)
            return f"Double solutions x1=x2={x}"
        else:
            x1 = round(((-b - sqrt(delta)) / (2 * a)),2)
            x2 = round(((-b + sqrt(delta)) / (2 * a)),2)
            return f"x1={x1}, x2={x2}"