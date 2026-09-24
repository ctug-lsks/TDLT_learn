def draw_fig (n):
    for i in range (0,n):
        for j in range (0,n):
            if j==0 or j ==n-1 or i==j:
                print ("*", end="")
            else:
                print (" ", end="")
        print()

draw_fig(7)
print()

def draw_fig_m(n):
    for i in range(0,n):
        for j in range(0,n):
            if j<(n/2):
                if j==0 or j==i:
                    print ("*", end="")
                else:
                    print (" ", end="")
            else:
                if j==n-1 or j+i==(n-1):
                    print ("*", end="")
                else:
                    print (" ", end="")
        print()
draw_fig_m (10)

