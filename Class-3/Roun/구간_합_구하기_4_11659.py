############
# silver 3 #
############

import sys

input = sys.stdin.readline

number_of_items, number_of_commands = map(int, input().split())

items = [0]
items.extend(map(int, input().split()))

sums = [0] * (number_of_items + 1)
for i in range(1, number_of_items + 1):
    sums[i] = sums[i - 1] + items[i]

for i in range(number_of_commands):
    start, end = map(int, input().split())
    print(sums[end] - sums[start - 1])

###################
# memory: 41144KB #
# time:   256ms   #
###################