n = int(input())
grid = [[0] * n for _ in range(n)]

x, y = n // 2, n // 2
move_dir, move_num = 0, 1 # 방향, 해당 방향으로 이동할 횟수

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def end():
    return not in_range(x, y)

def move():
    global x, y
    dxs, dys = [0, -1, 0, 1], [1, 0, -1, 0]
    x, y = x + dxs[move_dir], y + dys[move_dir]

cnt = 1 # 해당 방향으로 이동할 횟수
while not end():
    for _ in range(move_num):
        grid[x][y] = cnt
        cnt += 1

        move()

        if end():
            break

    move_dir = (move_dir + 1) % 4
    if move_dir == 0 or move_dir == 2:
        move_num += 1

for row in grid:
    for col in row:
        print(col, end=' ')
    print()