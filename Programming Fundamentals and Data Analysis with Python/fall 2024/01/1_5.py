n = int(input())
if n!=0:
    for a in range(0, n):
        s=""
        m=int(input())
        for i in range(1, m + 1, 1):
            s += str(i)
            s += " "
        print(s)
else:
    print("")