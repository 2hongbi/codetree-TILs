st = input()

ans = 0

for i in range(len(st)):
    if st[i] == '(':
        ans += st[i+1:].count(')')

print(ans)