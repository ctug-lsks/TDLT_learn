from review_midterm.midterm1.Q1.Q1 import calc_NPV, is_investment

c0=10000
ct=4250
t=3
r=0.07
NPV=calc_NPV(c0,ct,r,t)
print(NPV)
is_investment(NPV)

