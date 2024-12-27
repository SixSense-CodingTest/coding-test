############
# silver 2 #
############

import sys
from collections import deque

def bfs(graph: list, start_point: tuple) -> set:
    visited = set([start_point])
    queue = deque([start_point])

    while queue:
        y, x = queue.popleft()

        # 상하좌우
        for dy, dx in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            next_y, next_x = y + dy, x + dx

            # 맵 안에 존재하는 좌표인지 확인
            if 0 <= next_y < len(graph) and 0 <= next_x < len(graph[0]):
                # 배추가 있고, 방문하지 않은 곳이라면 queue와 visited에 추가
                if graph[next_y][next_x] == 1 and (next_y, next_x) not in visited:
                    queue.append((next_y, next_x))
                    visited.add((next_y, next_x))

    return visited


def solve(graph: list) -> int:
    visited = set()
    count = 0

    # 0, 0부터 방문하지 않은 배추가 있는 곳 탐색
    for i in range(len(graph)):
        for j in range(len(graph[0])):
            if graph[i][j] == 1 and (i, j) not in visited:
                # 한 번의 방문으로 이어진 배추 모두 방문 처리를 위해 union 연산
                visited = visited.union(bfs(graph, (i, j)))
                # 방문 횟수 증가
                count += 1

    return count

input = sys.stdin.readline

number_of_cases = int(input())

for _ in range(number_of_cases):
    col, row, points = map(int, input().split())

    graph = [[0 for i in range(col)] for j in range(row)]

    for p in range(points):
        x, y = map(int, input().split())
        graph[y][x] = 1

    print(solve(graph))

###################
# memory: 34992KB #
# time:   72ms    #
###################