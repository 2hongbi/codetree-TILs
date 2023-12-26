st = input()

answer = 0
for i in range(len(st)):
    if st[i] == '(':
        answer += st[i + 1:].count(')')

print(answer)