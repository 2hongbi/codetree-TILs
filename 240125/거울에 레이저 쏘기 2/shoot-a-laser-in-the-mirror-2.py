n = int(input())

grid = [
    input()
    for _ in range(n)
]

start_num = int(input())

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def initialize(num):
    # return x, y, move_dir
    if num <= n:
        return 0, num - 1, 0
    elif num <= 2 * n:
        return num - n - 1, n - 1, 1
    elif num <= 3 * n:
        return n - 1, n - (num - 2 * n), 2
    else:
        return n - (num - 3 * n), 0, 3

def move(x, y, next_dir):
    dxs, dys = [1, 0, -1, 0], [0, -1, 0, 1]
    nx, ny = x + dxs[next_dir], y + dys[next_dir]
    return nx, ny, next_dir

def simulate(x, y, move_dir):
    move_num = 0
    while in_range(x, y):
        if grid[x][y] == '/':
            x, y, move_dir = move(x, y, move_dir ^ 1)
        else:
            x, y, move_dir = move(x, y, 3 - move_dir)
        move_num += 1
    return move_num

x, y, move_dir = initialize(start_num)
move_num = simulate(x, y, move_dir)
print(move_num)