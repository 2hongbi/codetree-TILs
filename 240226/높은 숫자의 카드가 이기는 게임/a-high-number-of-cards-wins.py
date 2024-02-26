n = int(input())
b_cards = [int(input()) for _ in range(n)]

a_cards = [i for i in range(1, 2 * n + 1) if i not in b_cards] 

a_score = 0

for i in range(n):
    a_card = a_cards.pop() # 가장 작은 숫자부터 추출
    b_card = b_cards.pop()

    if a_card > b_card:
        a_score += 1


print(a_score)