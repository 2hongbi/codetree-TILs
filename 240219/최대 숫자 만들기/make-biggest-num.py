n = int(input())
numbers = [input() for _ in range(n)]

numbers.sort(key=lambda x: x * 4, reverse=True)
print(int(''.join(numbers)))