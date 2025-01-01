############
# silver 2 #
############

import sys

input = sys.stdin.readline

number_of_items = int(input())

items = list(map(int, input().split()))

rank = sorted(list(set(items)))
rank = {item: i for i, item in enumerate(rank)}

for item in items:
    print(rank[item], end=' ')

####################
# memory: 149248KB #
# time:   1924ms   #
####################