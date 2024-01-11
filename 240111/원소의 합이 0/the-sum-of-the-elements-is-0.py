from collections import defaultdict

n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))
D = list(map(int, input().split()))

hashmap = defaultdict(int)

for a in A:
    for b in B:
        hashmap[a + b] += 1

count = 0
for c in C:
    for d in D:
        count += hashmap[-(c + d)]

print(count)