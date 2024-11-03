N = int(input())
min_values = []
for _ in range(N):
    numbers = list(map(float, input().split()))
    min_values.append(min(numbers))
result = max(min_values)
print(f"{result:.3f}")
