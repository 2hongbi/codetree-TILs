from collections import defaultdict

string = input()

hashmap = defaultdict(int)
for s in string:
    hashmap[s] += 1

ans = False
for k, v in hashmap.items():
    if v == 1:
        print(k)
        ans = True
        break

if not ans:
    print('None')