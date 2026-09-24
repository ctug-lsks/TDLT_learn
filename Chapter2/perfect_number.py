x = 0
while x == 0:
    n=int(input("Nhập vào n (n>0): "))
    sum = 1
    i = 2
    while i<n:
        if n%i == 0:
            sum +=i
        i+=1
    if sum == n and sum != 1:
        print (f"{n} là số hoàn thiện")
    else:
        print (f"{n} không phải là số hoàn thiện")