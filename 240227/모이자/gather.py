import sys

n = int(input())
houses = list(map(int, input().split()))

dist = sys.maxsize

for i in range(n):
    temp = 0
    for j in range(n):
        move = abs(i - j)
        temp += move * houses[j]
    dist = min(dist, temp)

print(dist)