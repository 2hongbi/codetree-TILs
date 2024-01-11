from collections import defaultdict

n = int(input())

hashmap = defaultdict(int)
for _ in range(n):
    temp = list(map(str, input()))
    temp.sort()
    hashmap[''.join(temp)] += 1

print(max(hashmap.values()))