############
# silver 4 #
############

import sys
from collections import deque

people, step = map(int, input().split())

queue = deque(range(1, people + 1))

result = "<"

while len(queue) > 1:
    queue.rotate(-(step - 1))
    result += f"{queue.popleft()}, "

result += f"{queue.popleft()}>"

print(result)

###################
# memory: 34900KB #
# time:   60ms    #
###################