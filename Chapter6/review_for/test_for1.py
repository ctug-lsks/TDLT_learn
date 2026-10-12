#print odd number from 1 to 2N+1 (N):
n=11
print("odd number")
for i in range(1,n,2):
    print(i, end=" ")

print("\neven number")
for i in range(2,n,2):
    print(i, end=" ")

print("\neven number")
for i in range(2,n,1):
    if i%2==0:
        print(i, end=" ")