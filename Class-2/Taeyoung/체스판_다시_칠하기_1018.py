import sys

input = sys.stdin.readline

N, M = map(int, input().split())


def check(y, x, start, map) -> int:
    diff = 0
    for i in range(8):
        for j in range(8):
            if start == 'B':
                gt = 'B' if (i+j) % 2 == 0 else 'W'
            elif start == 'W':
                gt = 'W' if (i+j) % 2 == 0 else 'B'

            if map[y+i][x+j] != gt:
                diff += 1

    return diff


min_change = N*M
map = [[i for i in input()] for j in range(N)]


for i in range(N-8+1):
    for j in range(M-8+1):
        start_B = check(i, j, 'B', map)
        start_W = check(i, j, 'W', map)
        min_change = min(min_change, start_B, start_W)

print(min_change)

####################
# memory: 32412KB  #
# time:   64ms     #
####################
