from collections import defaultdict

n, k = map(int, input().split())
numbers = list(map(int, input().split()))

num_dict = defaultdict(int)
for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        tmp = numbers[i] + numbers[j]
        num_dict[tmp] += 1

print(num_dict[k])