n = int(input())

def min_coins(n):
    five_count = n // 5
    remainder = n % 5

    while five_count >= 0:
        if remainder % 2 == 0:
            two_count = remainder // 2
            return five_count + two_count
        five_count -= 1
        remainder += 5
    
    return -1

print(min_coins(n))