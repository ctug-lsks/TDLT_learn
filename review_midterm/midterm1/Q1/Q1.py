def calc_NPV(c0, ct, r, t):
    sum_ct=0
    i=1
    while i<=t:
        result=ct/(1+r)**i
        sum_ct+=result
        i+=1
    NPV=sum_ct-c0
    return NPV

def is_investment(NPV):
    if NPV>0:
        print("The project can be invested")
        return "The project can be invested"
    elif NPV<0:
        print("The project can not be invested")
        return "The project can not be invested"
    elif NPV==0:
        print("Depend on you")
        return "Depend on you"
