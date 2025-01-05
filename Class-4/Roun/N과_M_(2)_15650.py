############
# silver 2 #
############

import sys

def solve(start_point: int, depth: int):
    global items, n, m

    if depth == m:
        print(*items)
        return

    for i in range(start_point, n + 1):
        items.append(i)
        solve(i + 1, depth + 1)
        items.pop()


input = sys.stdin.readline

n, m = map(int, input().split())

items = []

solve(1, 0)

###################
# memory: 32412KB #
# time:   40ms    #
###################