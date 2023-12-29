from collections import defaultdict

n, m = map(int, input().split())
numbers = list(map(int, input().split()))

num_cnt_dict = defaultdict(int)
for n in numbers:
    num_cnt_dict[n] += 1

target = map(int, input().split())
# for t in target:
    # answer.append(numbers.count(t))

for t in target:
    print(num_cnt_dict[t], end=' ')

# print(' '.join(list(map(str, answer))))