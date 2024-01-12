commands = list(map(str, input()))

x, y = 0, 0
dir_num = 3
dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]

for command in commands:
    if command == 'L':
        dir_num = (dir_num - 1 + 4) % 4
    elif command == 'R':
        dir_num = (dir_num + 1) % 4
    elif command == 'F':
        x, y = x + dx[dir_num], y + dy[dir_num]

print(x, y)