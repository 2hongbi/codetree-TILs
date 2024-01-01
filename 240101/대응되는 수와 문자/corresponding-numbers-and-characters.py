n, m = map(int, input().split())

num_idx_dict = {}
str_idx_dict = {}
for i in range(n):
    temp = input()
    num_idx_dict[i + 1] = temp
    str_idx_dict[temp] = i + 1

for _ in range(m):
    target = input()
    if target.isalpha():
        print(str_idx_dict[target])
    else:
        print(num_idx_dict[int(target)])