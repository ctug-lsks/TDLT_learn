x=int(input("Enter x:"))
n=int(input("Enter n:"))
S=0
i=1
while i<=n:
    S=S+pow(x,i)
    i+=1
print(f"S{x,n}={S}")
