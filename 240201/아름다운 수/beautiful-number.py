def check_beautiful_number(position, last_number, length, n, results):
    if position == n:
        if last_number == length:  # 마지막 숫자의 길이가 숫자와 일치하는지 확인
            return results + 1
        else:
            return results
    
    total = 0
    # 현재 숫자가 이전 숫자와 동일한 경우
    if length < last_number:
        total += check_beautiful_number(position + 1, last_number, length + 1, n, results)
    # 새 숫자를 시작하는 경우
    for i in range(1, 5):  # 1부터 4까지의 숫자 사용
        if i != last_number:  # 연속되지 않는 새 숫자를 시작
            total += check_beautiful_number(position + 1, i, 1, n, results)
    return total

n = int(input())
results = check_beautiful_number(0, 0, 0, n, 0)
print(results)