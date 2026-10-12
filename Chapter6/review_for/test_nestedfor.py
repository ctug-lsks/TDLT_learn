# n=int(input("Enter a number: "))
# for i in range(0,n):
#     for j in range(0,n):
#         if i==n-1 or j==n-1 or i+j==n-1:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()
#
# def draw_fig_m2(n):
#     for i in range(0,n):
#         for j in range(0,n):
#             if j<(n/2):
#                 if j==0 or j==i:
#                     print ("*", end="")
#                 else:
#                     print (" ", end="")
#             else:
#                 if j==n-1 or j+i==(n-1):
#                     print ("*", end="")
#                 else:
#                     print (" ", end="")
#         print()
# draw_fig_m2 (7)
#
# def draw_fig_m(n):
#     for i in range(0,n):
#         for j in range(0,n):
#             if j==0 or (j==i and i<=n//2) or j==n-1 or (j+i==n-1 and i<=n//2):
#                 print ("*", end="")
#             else:
#                 print (" ", end="")
#         print()
# draw_fig_m (7)

# def draw_fig_in(n):
#     for i in range ()

n = 11
if n <= 0 or n % 2 == 0:
    print("n phải là số lẻ dương")
else:
    mid = n // 2
    for i in range(0, n):
        row = ""
        for j in range(0, n):
            if abs(i - mid) + abs(j - mid) >= mid:
                row += "* "
            else:
                row += "  "
        print(row)