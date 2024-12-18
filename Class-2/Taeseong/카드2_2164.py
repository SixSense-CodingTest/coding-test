from collections import deque

cards = deque(range(1,int(input())+1))

while len(cards)>1:
    cards.popleft()
    cards.append(cards.popleft())

print(cards[0])