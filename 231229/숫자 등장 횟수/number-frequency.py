n, m = map(int, input().split())
numbers = list(map(int, input().split()))

answer = []
target = map(int, input().split())
for t in target:
    answer.append(numbers.count(t))

print(' '.join(list(map(str, answer))))