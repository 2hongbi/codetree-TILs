n = int(input())
numbers = [input() for _ in range(n)]

numbers.sort(key=lambda x: x * 10, reverse=True)

print(int(''.join(numbers)))