def find_max(a):
    # a를 list로 변환
    a_list = list(a)

    max_val = int(''.join(a_list), 2)

    # '0'이 나오는 첫 번째 위치를 찾아 '1'로 변경
    for i in range(len(a_list)):
        if a_list[i] == '0':
            a_list[i] = '1'
            max_val = max(max_val, int(''.join(a_list), 2))
            a_list[i] = '0'

    return max_val


n = input()
print(find_max(n))