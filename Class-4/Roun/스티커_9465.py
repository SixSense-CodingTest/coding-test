############
# silver 1 #
############

import sys

input = sys.stdin.readline

number_of_cases = int(input())

for _ in range(number_of_cases):

    col = int(input())
    dp = [[0] * col for _ in range(2)]

    items = []

    for i in range(2):
        items.append(list(map(int, input().split())))

    # 이전 값 저장
    prev = [items[0][0], items[1][0]]
    # 현재 값 저장
    curr = [0, 0]

    # 2 이상인 경우, 현재값 초기화
    if col > 1:
        curr[0] = prev[1] + items[0][1]
        curr[1] = prev[0] + items[1][1]

    # 3부터는 위쪽을 선택할 경우 이전 또는 현재의 아랫값 중 최댓값을 선택
    # 아래쪽을 선택할 경우 이전 또는 현재의 윗값 중 최댓값을 선택 max(전전 윗값, 이전 윗값) + 현재 아랫값
    for i in range(2, col):
        _next = [max(prev[1], curr[1]) + items[0][i], max(prev[0], curr[0]) + items[1][i]]

        prev = curr
        curr = _next
    

    if col == 1:
        print(max(prev))
    else:
        print(max(curr))

###################
# memory: 41782KB #
# time:   580ms   #
###################