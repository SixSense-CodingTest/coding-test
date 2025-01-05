############
# silver 3 #
############

import sys

def solve(depth: int):
    global result, items, number_of_items, number_of_selections

    if depth == number_of_selections:
        print(*result)
        return

    for i in range(number_of_items):
        if items[i] in result:
            continue
        result.append(items[i])
        solve(depth + 1)
        result.pop()

input = sys.stdin.readline

number_of_items, number_of_selections = map(int, input().split())

items = sorted(list(map(int, input().split())))

result = []

solve(0)

###################
# memory: 32412KB #
# time:   204ms   #
###################