n, k = map(int, input().split())
numbers = list(map(int, input().split()))

num_dict = dict()

ans = 0
for num in numbers:
    diff = k - num
    if diff in num_dict:
        ans += num_dict[diff]
    if num in num_dict:
        num_dict[num] += 1
    else:
        num_dict[num] = 1


print(ans)