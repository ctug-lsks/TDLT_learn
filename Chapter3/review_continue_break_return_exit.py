n=10
sum =0
for i in range (1,n+1):
    if i%2 !=0:
        continue
    sum+=1
print ("sum", sum)

gpa=-1
while gpa<0 or gpa>10:
    gpa=int(input("Nhập GPA:"))
print("GPA:",gpa)

drl=-1
while True:
    drl=int(input("Nhập ĐRL:"))
    if drl>=0 and drl<=100:
        break
print("ĐRL:", drl)