############
# silver 4 #
############

import sys

input = sys.stdin.readline

def get_minimum(graph: list, start_point: tuple = (0, 0)):

    start_y, start_x = start_point

    white_first_count = 0
    black_first_count = 0

    for y in range(start_y, start_y + 8):
        for x in range(start_x, start_x + 8):
            current_color = graph[y][x]
            # white_first_expected color
            expected_white = 'W' if (y + x) % 2 == 0 else 'B'  
            # black_first_expected color
            expected_black = 'B' if (y + x) % 2 == 0 else 'W' 

            if current_color != expected_white:
                white_first_count += 1
            if current_color != expected_black:
                black_first_count += 1

    return min(white_first_count, black_first_count)

row, col = map(int, input().split())
graph = []

for i in range(row):
    graph.append(list(input().rstrip()))

min_value = float('inf')

for y in range(row + 1 - 8):
    for x in range(col + 1 - 8):
        min_value = min(min_value, get_minimum(graph, (y, x)))

print(min_value)

###################
# memory: 32412KB #
# time:   60ms    #
###################

