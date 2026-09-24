x=0
while x == 0:
    n = int (input("nhập n: "))
    count = 1
    i = 1
    while i < n:
        if n % i == 0:
            count += 1
        i += 1
    if count == 2:
        print(n,"là số nguyên tố")
    else:
        print(n,"không phải số nguyên tố")