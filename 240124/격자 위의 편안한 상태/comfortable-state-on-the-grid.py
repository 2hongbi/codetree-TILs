n, m = map(int, input().split())

grid = [
    [0] * n
    for _ in range(n)
]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def check_status(x, y):
    check = 0

    dxs, dys = [-1, 0, 1, 0], [0, 1, 0, -1]
    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy
        if in_range(nx, ny) and grid[nx][ny] == 1:
            check += 1
    
    if check == 3:
        return True
    return False
        


for _ in range(m):
    r, c = map(int, input().split())
    if check_status(r - 1, c - 1):
        print(1)
    else:
        print(0)
    grid[r - 1][c - 1] = 1