n = int(input())
arr1 = list(map(int, input().split()))

m = int(input())
arr2 = list(map(int, input().split()))

set1 = set(arr1)

for a in arr2:
    if a in set1:
        print(1, end=' ')
    else:
        print(0, end=' ')