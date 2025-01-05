##########
# gold 4 #
##########

import sys
from collections import deque

def bfs(graph: list, start_point: tuple) -> int:
    global total_visited
    result = 0

    queue = deque([(*start_point, set([start_point]), graph[start_point[0]][start_point[1]])])

    while queue:
        # print(queue)

        curr_y, curr_x, visited, score = queue.popleft()

        if len(visited) == 4:
            result = max(result, score)
            total_visited.append(visited)
            continue
        elif len(visited) == 2:
            targets = []
            for dy, dx in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                next_y, next_x = curr_y + dy, curr_x + dx

                if 0 <= next_y < len(graph) and 0 <= next_x < len(graph[0]) and (next_y, next_x) not in visited:
                    next_visited = visited.union(set([(next_y, next_x)]))
                    queue.append((next_y, next_x, next_visited, score + graph[next_y][next_x]))

                    targets.append((next_y, next_x))
            
            for i in range(len(targets)):
                for j in range(i + 1, len(targets)):
                    result = max(result, score + graph[targets[i][0]][targets[i][1]] + graph[targets[j][0]][targets[j][1]])
        else:
            for dy, dx in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                next_y, next_x = curr_y + dy, curr_x + dx

                if 0 <= next_y < len(graph) and 0 <= next_x < len(graph[0]) and (next_y, next_x) not in visited:
                    next_visited = visited.union(set([(next_y, next_x)]))
                    if next_visited not in total_visited:
                        queue.append((next_y, next_x, next_visited, score + graph[next_y][next_x]))
            
        

    return result

def solve(graph: list) -> int:
    result = 0

    for i in range(len(graph)):
        for j in range(len(graph[0])):
            result = max(result, bfs(graph, (i, j)))


    return result

input = sys.stdin.readline

row, col = map(int, input().split())
graph = []
total_visited = []

for _ in range(row):
    graph.append(list(map(int, input().split())))

print(solve(graph))
print(total_visited)