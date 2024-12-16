############
# bronze 1 #
############

import sys
import math

input = sys.stdin.readline

numbers, selects = map(int, input().rstrip().split())

up = math.prod(range(numbers, numbers-selects, -1))
down = math.prod(range(selects, 1, -1))

print(up // down)

###################
# memory: 34536KB #
# time:   36ms    #
###################