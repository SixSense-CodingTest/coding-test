import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

cards = deque(range(1, N + 1))

while len(cards) > 1:
    cards.popleft()
    cards.append(cards.popleft())

print(cards[0])

####################
# memory: 51848KB  #
# time:   164ms    #
####################
