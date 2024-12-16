##########
# gold 5 #
##########

import sys

sys.setrecursionlimit(10**6)

input = sys.stdin.readline

n, r, c = map(int, input().split())

depth = [2**i for i in range(n+1)]
row_pos = [2**(i*2 + 1) for i in range(1, n+1)]
col_pos = [2**(i*2) for i in range(1, n+1)]

# print(depth)
# print(row_pos)
# print(col_pos)

default = dict()
default[(0, 0)] = 0
default[(0, 1)] = 1
default[(1, 0)] = 2
default[(1, 1)] = 3

def find_max_sub(target: int):
    global depth

    for item in reversed(depth):
        if item <= target:
            return item
        
    return 0


def recursion(point: tuple):
    global default
    global depth
    # print(point)
    if point in default.keys():
        return default[point]
    
    row, col = point
    row_sub, col_sub = 0, 0
    summation = 0

    if row > 1:
        row_sub = find_max_sub(row)
        summation += row_pos[depth.index(row_sub) - 1]
    if col > 1:
        col_sub = find_max_sub(col)
        summation += col_pos[depth.index(col_sub) - 1]

    # print(f'row_sub: {row_sub}, col_sub: {col_sub}')
    # print(f'summation: {summation}')

    return recursion((row - row_sub, col - col_sub)) + summation
   

print(recursion((r, c)))

###################
# memory: 32412KB #
# time:   40ms    #
###################

# 우여곡절 끝에 풀었지만 뭔가 엉성한 부분이 존재함 (나중에 다시 풀어보자.)
# solution:
# (7, 7)이 주어졌다면 재귀적으로 (3, 3) -> (1, 1)을 찾아나간다.
# 그 값의 차이만큼을 더해준다.