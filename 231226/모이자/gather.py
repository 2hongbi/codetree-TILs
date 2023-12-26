n = int(input())
nums = list(map(int, input().split()))

answer = []
for i in range(n):
    temp = 0
    for j in range(n):
        temp += nums[j] * abs(j - i)
    answer.append(temp)

print(min(answer))