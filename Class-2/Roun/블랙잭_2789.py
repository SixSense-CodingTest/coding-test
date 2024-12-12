############
# bronze 2 #
############

import sys

input = sys.stdin.readline

number_of_cards, target = map(int, input().rstrip().split())

cards = sorted(list(map(int, input().rstrip().split())))

ans = 0

for i, card in enumerate(cards):
    # 첫 카드가 target을 넘으면 탐색할 이유가 없음
    if card > target:
        break

    start, end = i + 1, number_of_cards - 1

    # 투포인터를 활용한 슬라이딩 윈도우 탐색
    while start < end:
        temp_ans = card + cards[start] + cards[end]

        if temp_ans <= target:
            ans = max(ans, temp_ans)
            start += 1
        else:
            end -= 1

print(ans)

###################
# memory: 32412KB #
# time:   32ms    #
###################