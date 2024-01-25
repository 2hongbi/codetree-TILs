n, m = map(int, input().split())

def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

def fill_grid(n, m):
    grid = [[0] * m for _ in range(n)]

    x, y = 0, 0
    dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]
    dir_num = 0

    for i in range(n * m):
        grid[x][y] = chr(65 + (i % 26))
        nx, ny = x + dxs[dir_num], y + dys[dir_num]

        if not in_range(nx, ny) or grid[nx][ny]!= 0:
            dir_num = (dir_num + 1) % 4
            nx, ny = x + dxs[dir_num], y + dys[dir_num]
        
        x, y = nx, ny
    
    return grid

result = fill_grid(n, m)
for r in result:
    for c in r:
        print(c, end=' ')
    print()