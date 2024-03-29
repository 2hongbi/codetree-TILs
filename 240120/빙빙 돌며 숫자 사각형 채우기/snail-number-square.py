n, m = map(int, input().split())

def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

grid = [
    [0] * m
    for _ in range(n)    
]

dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]
x, y = 0, 0
dir_num = 0
grid[x][y] = 1

for i in range(2, n * m + 1):
    nx, ny = x + dxs[dir_num], y + dys[dir_num]

    if not in_range(nx, ny) or grid[nx][ny] != 0:
        dir_num = (dir_num + 1) % 4

    x, y = x + dxs[dir_num], y + dys[dir_num]
    grid[x][y] = i

for i in range(n):
    for j in range(m):
        print(grid[i][j], end=' ')
    print()