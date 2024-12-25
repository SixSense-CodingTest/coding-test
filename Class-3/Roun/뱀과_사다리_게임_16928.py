##########
# gold 5 #
##########

import sys
from collections import deque

input = sys.stdin.readline

def bfs(graph: dict, start_point: int = 1, target_point: int = 100) -> int:
    queue = deque([(start_point, 0)])
    visited = set([start_point])

    while queue:
        curr_pos, depth = queue.popleft()

        if curr_pos == target_point:
            return depth

        for dx in [1, 2, 3, 4, 5, 6]:
            next_pos = curr_pos + dx

            if next_pos in graph.keys():
                next_pos = graph[next_pos]

            if next_pos <= target_point and next_pos not in visited:
                visited.add(next_pos)
                queue.append((next_pos, depth + 1))

    return -1



number_of_ladders, number_of_snakes = map(int, input().split())

graph = {}

for i in range(number_of_ladders):
    start, end = map(int, input().split())

    graph[start] = end

for i in range(number_of_snakes):
    start, end = map(int, input().split())

    graph[start] = end

print(bfs(graph=graph, start_point=1, target_point=100))

###################
# memory: 35092KB #
# time:   64ms    #
###################

# 주사위를 던져 이동한 위치에 사다리 또는 뱀이 있는 경우 그 위치로 이동하는 작업 필요