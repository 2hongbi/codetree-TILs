n = input()

max_val = int(n, 2)

for i in range(len(n)):
    temp = list(n)
    if temp[i] == '0':
        temp[i] = '1'
    else:
        temp[i] = '0'
    max_val = max(max_val, int(''.join(temp), 2))

print(max_val)