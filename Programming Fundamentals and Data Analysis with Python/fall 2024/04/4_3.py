b1, q, N = map(float, input().split())
S = b1 * (1 - q**N) / (1 - q) if q != 1 else b1 * N
print(f"{S:.3f}")