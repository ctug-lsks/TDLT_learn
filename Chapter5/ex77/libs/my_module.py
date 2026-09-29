def cal_operations(a,b,button):
    if button == "+":
        return f"a+b={a+b}"
    elif button == "-":
        return f"a-b={a-b}"
    elif button == "*":
        return f"a*b={a*b}"
    elif button == "/":
        return f"a/b={a/b}"


def do_math(a,b,op):
    match op:
        case "+":
            return f"{a}+{b}={a+b}"
        case "-":
            return f"{a}-{b}={a-b}"
        case "*":
            return f"{a}*{b}={a*b}"
        case "/":
            if b==0:
                return "can't divide by zero"
            return f"{a}//{b}={a//b}"
        case _:
            return "can not do the math"