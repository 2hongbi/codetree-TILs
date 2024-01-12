n, t = map(int, input().split())
x, y, dir = input().split()

directions = {'U': 0, 'R': 1, 'D': 3, 'L': 2}

dxs, dys = [-1, 0, 0, 1], [0, 1, -1, 0]

def in_range(x, y):
    return 1 <= x <= n and 1 <= y <= n

dir_num = directions[dir]
x, y = int(x), int(y)

for _ in range(t):
    nx, ny = x + dxs[dir_num], y + dys[dir_num]
    if in_range(nx, ny):
        x, y = nx, ny
    else:
        dir_num = 3 - dir_num

print(x, y)