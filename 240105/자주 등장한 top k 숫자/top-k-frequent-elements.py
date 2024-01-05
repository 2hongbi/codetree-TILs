n, k = map(int, input().split())
numbers = list(map(int, input().split()))

count = dict()
for num in numbers:
    count[num] = count.get(num, 0) + 1

answer = []
for key, value in count.items():
    if value == k:
        answer.append(key)

answer.sort(reverse=True)
for a in answer:
    print(a, end=' ')