n, k = map(int, input().split())
numbers = list(map(int, input().split()))

count = dict()
for num in numbers:
    count[num] = count.get(num, 0) + 1

sorted_cnt = sorted(count.items(), key=lambda x: (-x[1], -x[0]))
sorted_keys = [key for key, value in sorted_cnt]

for key in sorted_keys[:k]:
    print(key, end=' ')