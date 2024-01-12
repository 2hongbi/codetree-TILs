n = int(input())
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n


def count_one(x, y):
    cnt = 0
    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy
        if in_range(nx, ny) and grid[nx][ny] == 1:
            cnt += 1

    return cnt


ans = 0
for i in range(n):
    for j in range(n):
        if count_one(i, j) >= 3:
            ans += 1

print(ans)