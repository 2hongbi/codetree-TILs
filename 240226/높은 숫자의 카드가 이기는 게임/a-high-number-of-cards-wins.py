n = int(input())
b_cards = [int(input()) for _ in range(n)]

a_cards = []
for i in range(1, 2 * n + 1):
    if i not in b_cards:
        a_cards.append(i)

a_cards.sort(reverse=True)

a_score = 0

for i in range(n):
    a_card = a_cards.pop()
    b_card = b_cards[i]

    if a_card > b_card:
        a_score += 1


print(a_score)