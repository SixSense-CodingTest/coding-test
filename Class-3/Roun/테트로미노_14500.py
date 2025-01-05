##########
# gold 4 #
##########

import sys
from collections import deque

def dfs(graph: list, start_point: tuple, depth: int, score: int) -> int:
    global result
    global visited

    y, x = start_point
    
    if depth == 4:
        result = max(result, score)
        return

    for dy, dx in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
        next_y, next_x = y + dy, x + dx

        if 0 <= next_x < len(graph[0]) and 0 <= next_y < len(graph) and not visited[next_y][next_x]:
            visited[next_y][next_x] = True
            dfs(graph, (next_y, next_x), depth + 1, score + graph[next_y][next_x])
            visited[next_y][next_x] = False

def fk(graph: list, start_point: tuple) -> int:
    global result, shapes

    y, x = start_point

    for shape in shapes:
        temp = graph[y][x]
        check = True

        for dy, dx in shape:
            next_y, next_x = y + dy, x + dx
            if 0 <= next_x < len(graph[0]) and 0 <= next_y < len(graph):
                temp += graph[next_y][next_x]
            else:
                check = False
                break
        
        if check:
            result = max(result, temp)



input = sys.stdin.readline

row, col = map(int, input().split())
graph = []
visited = [[False for i in range(col)] for j in range(row)]
result = 0

shapes = [
    [(-1, 0), (0, -1), (0, 1)], # ㅓ
    [(1, 0), (0, -1), (0, 1)], # ㅏ
    [(0, -1), (-1, 0), (1, 0)], # ㅗ
    [(0, 1), (-1, 0), (1, 0)] # ㅜ
]

for _ in range(row):
    graph.append(list(map(int, input().split())))

for i in range(row):
    for j in range(col):
        visited[i][j] = True
        dfs(graph, (i, j), 1, graph[i][j])
        visited[i][j] = False

        fk(graph, (i, j))

print(result)

###################
# memory: 40212KB #
# time:   5444ms  #
###################

# dfs로 일반적인 모양 처리
# (dfs로 처리하므로 backtracking 활용해야해 visited 관리해야함 1개의 모양에 대해 탐색이 완료되면 다시 되돌려야하므로)
# ㅗ모양 별도 처리 depth 2에서 갈 수 있는 2개의 방향을 탐색할까 했지만 미리 정의해두고 하는게 더 빠를 듯
# 나중에 다시 구현해보자.