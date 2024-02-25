p = int(input("N : "))
l = int(input("M : "))
t = int(input("L : "))

x = p - t
for i in range (p):
    for j in range (l):
        if (t <= i < x):
            if(j < t):
                print("*",end="")
            else:
                print(".",end="")
        else:
            print("*",end="")
    print()
