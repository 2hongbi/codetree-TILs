from collections import defaultdict

n = int(input())

def default_value():
    return 100001

coordinate = defaultdict(default_value)
for _ in range(n):
    x, y = map(int, input().split())
    coordinate[x] = min(y, coordinate[x])

total = 0
for v in coordinate.values():
    total += v

print(total)