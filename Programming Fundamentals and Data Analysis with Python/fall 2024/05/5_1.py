start, stop, step = map(int, input().split())
n = list(map(int, input().split()))
progression = range(start, stop, step)
for i in progression:
    n[i] = i
print(n)