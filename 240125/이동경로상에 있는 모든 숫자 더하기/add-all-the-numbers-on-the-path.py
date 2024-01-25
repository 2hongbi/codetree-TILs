n, t = map(int, input().split())
commands = input()
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

x, y = n // 2, n // 2
dxs, dys = [-1, 0, 1, 0], [0, 1, 0, -1]
move_dir = 0

ans = grid[x][y]

for cmd in commands:
    if cmd == 'L':
        move_dir = (move_dir - 1 + 4) % 4
    elif cmd == 'R':
        move_dir = (move_dir + 1) % 4
    elif cmd == 'F':
        nx, ny = x + dxs[move_dir], y + dys[move_dir]
        
        if in_range(nx, ny):
            ans += grid[nx][ny]
            x, y = nx, ny

print(ans)