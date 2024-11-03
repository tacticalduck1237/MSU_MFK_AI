limit, N = map(int, input().split())
total_cost = 0
for _ in range(N):
    slots = input().split()
    min_cost = float('inf')
    for slot in slots:
        price, quantity = map(int, slot.split('/'))
        if price <= limit:
            cost = price * quantity
            if cost < min_cost:
                min_cost = cost
    if min_cost != float('inf'):
        total_cost += min_cost
print(total_cost)