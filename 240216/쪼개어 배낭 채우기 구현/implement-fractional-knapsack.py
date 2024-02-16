n, m = map(int, input().split())
jewels = []

for _ in range(n):
    w, v = map(int, input().split())
    jewels.append((v / w, w, v))

jewels.sort(reverse=True)

total = 0
for density, weight, value in jewels:
    if m >= weight:
        total += value
        m -= weight
    else:
        # 가방에 보석을 일부만 담을 수 있는 경우
        total += density * m
        break

print(f'{total:.3f}')