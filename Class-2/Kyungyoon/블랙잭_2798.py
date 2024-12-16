from itertools import combinations

N, M = map(int, input().split( ))
card_list = list(map(int, input().split( )))

max = 0
for card in combinations(card_list, 3):
  card_sum = sum(card)
  if card_sum <= M and max < card_sum:
    max = card_sum
print(max)