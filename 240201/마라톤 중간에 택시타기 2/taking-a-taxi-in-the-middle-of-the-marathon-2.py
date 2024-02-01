import sys

n = int(input())
start_points = [tuple(map(int, input().split())) for _ in range(n)]

ans = sys.maxsize

# 1번과 n번 포인트는 건너뛰면 안됨
for idx in range(1, n - 1):
    temp_x, temp_y = 0, 0
    total = 0

    for i in range(n):
        if i == idx:
            continue
        x, y = start_points[i]
        total += abs(x - temp_x) + abs(y - temp_y)
        temp_x, temp_y = x, y

    ans = min(ans, total)

print(ans)