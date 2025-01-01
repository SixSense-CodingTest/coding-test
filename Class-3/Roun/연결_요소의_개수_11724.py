############
# silver 2 #
############

import sys
from collections import deque

def bfs(graph: list, start_point: int) -> set:
    visited = set([start_point])
    queue = deque([start_point])

    while queue:
        curr = queue.popleft()

        for i in range(1, len(graph)):
            if graph[curr][i] and i not in visited:
                visited.add(i)
                queue.append(i)
    
    return visited


def solve(graph: list) -> int:
    global number_of_points
    visited = set()
    count = 0

    for i in range(1, number_of_points + 1):
        if i not in visited:
            count += 1
            visited = visited.union(bfs(graph, i))

    return count


input = sys.stdin.readline

number_of_points, number_of_links = map(int, input().split())
graph = [[False for i in range(number_of_points + 1)] for j in range(number_of_points + 1)]

for _ in range(number_of_links):
    point1, point2 = map(int, input().split())

    graph[point1][point2] = True
    graph[point2][point1] = True

print(solve(graph))

###################
# memory: 41148KB #
# time:   632ms   #
###################