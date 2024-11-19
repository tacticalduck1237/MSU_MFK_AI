import math

# Function definition
def f(x):
    return math.sin(math.tan(1 + x / 1000))

# Bisection method
def bisection(a, b, epsilon=1e-7):
    while b - a > epsilon:
        mid = (a + b) / 2
        if f(a) * f(mid) < 0:
            b = mid
        else:
            a = mid
    return (a + b) / 2

# Input reading
N = int(input("Enter the number of intervals: "))
intervals = [tuple(map(float, input().split())) for _ in range(N)]

# Finding and printing roots
for a, b in intervals:
    root = bisection(a, b)
    print(f"{root:.6f}")
