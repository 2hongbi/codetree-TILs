n = int(input())

min_y = {}
for _ in range(n):
    x, y = map(int, input().split())
    
    if x not in min_y:
        min_y[x] = y
    else:
        min_y[x] = min(min_y[x], y)

total = 0
for v in min_y.values():
    total += v

print(total)