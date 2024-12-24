##########
# gold 5 #
##########

import sys
from collections import deque

input = sys.stdin.readline

# 일반 사람 기준 bfs -> 같은 색이 같은 영역
def basic_bfs(graph: list, start_point: tuple) -> int:
    global basic_visited
    
    color = graph[start_point[0]][start_point[1]]
    basic_visited.add(start_point)
    queue = deque([start_point])

    while queue:
        y, x = queue.popleft()

        for dy, dx in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
            new_y, new_x = y + dy, x + dx

            if 0 <= new_y < len(graph) and 0 <= new_x < len(graph[0]):
                if (new_y, new_x) not in basic_visited and graph[new_y][new_x] == color:
                    queue.append((new_y, new_x))
                    basic_visited.add((new_y, new_x))
    
    return 1

# 적록색약 기준 bfs -> R과 G가 같은 영역
def color_bfs(graph: list, start_point: tuple) -> int:
    global color_visited
    
    color = graph[start_point[0]][start_point[1]]

    if color == 'R' or color == 'G':
        colors = ['R', 'G']
    else:
        colors = ['B']

    color_visited.add(start_point)
    queue = deque([start_point])

    while queue:
        y, x = queue.popleft()

        for dy, dx in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
            new_y, new_x = y + dy, x + dx

            if 0 <= new_y < len(graph) and 0 <= new_x < len(graph[0]):
                if (new_y, new_x) not in color_visited and graph[new_y][new_x] in colors:
                    queue.append((new_y, new_x))
                    color_visited.add((new_y, new_x))

    return 1
    

def solve(graph: list) -> tuple:
    global basic_visited
    global color_visited

    basic_count = 0
    color_count = 0

    for i in range(len(graph)):
        for j in range(len(graph[0])):
            if (i, j) not in basic_visited:
                basic_count += basic_bfs(graph, (i, j))
            if (i, j) not in color_visited:
                color_count += color_bfs(graph, (i, j))

    return (basic_count, color_count)


num = int(input())
graph = []

basic_visited = set()
color_visited = set()

for i in range(num):
    graph.append(input().strip())

print(' '.join(map(str, solve(graph=graph))))

###################
# memory: 35664KB #
# time:   76ms    #
###################