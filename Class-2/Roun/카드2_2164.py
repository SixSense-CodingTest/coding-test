############
# silver 4 #
############

import sys
from collections import deque

input = sys.stdin.readline

num = int(input())

cards = deque(i for i in range(1, num+1))

while len(cards) > 1:
    cards.popleft()
    cards.append(cards.popleft())

print(cards.popleft())

###################
# memory: 51848KB #
# time:   184ms   #
###################