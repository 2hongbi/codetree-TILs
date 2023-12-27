a = input()

max_a = int(a, 2)

for i in range(len(a)):
    if a[i] == '0':
        temp = a[:i] + '1' + a[i+1:]
        max_a = max(max_a, int(temp, 2))

print(max_a)