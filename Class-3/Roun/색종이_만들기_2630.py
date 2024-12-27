############
# silver 2 #
############

import sys

def solve(graph: list, start_point: tuple, size: int) -> int:
    global total

    start_y, start_x = start_point

    color = graph[start_y][start_x]

    for i in range(start_y, start_y+size):
        for j in range(start_x, start_x+size):
            if graph[i][j] != color:
                half = size // 2
                solve(graph, (start_y, start_x), half)
                solve(graph, (start_y + half, start_x), half)
                solve(graph, (start_y, start_x + half), half)
                solve(graph, (start_y + half, start_x + half), half)
                return
            
    total[color] += 1


input = sys.stdin.readline

graph = []
total = [0, 0]

num = int(input())

for _ in range(num):
    graph.append(list(map(int, input().split())))

solve(graph, (0, 0), num)

print('\n'.join(map(str, total)))

###################
# memory: 32412KB #
# time:   48ms    #
###################