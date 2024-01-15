n = int(input())

hashset = set()
for _ in range(n):
    cmd, num = input().split()
    num = int(num)

    if cmd == 'find':
        if num in hashset:
            print('true')
        else:
            print('false')
    elif cmd == 'add':
        hashset.add(num)
    elif cmd == 'remove':
        hashset.remove(num)