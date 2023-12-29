from collections import defaultdict

count_dict = defaultdict(int)

n = int(input())
for _ in range(n):
    count_dict[input()] += 1

max_cnt = 0
for v in count_dict.values():
    max_cnt = max(max_cnt, v)

print(max_cnt)