############
# silver 3 #
############

import sys
from collections import deque

input = sys.stdin.readline

def bfs(graph: dict, start_point: int) -> int:
    visited = set([start_point])
    queue = deque([start_point])

    while queue:
        curr = queue.popleft()

        # queue에 아직 방문하지 않은 curr과 연결된 컴퓨터 추가
        queue.extend(graph[curr] - visited)
        # 추가된 컴퓨터 방문 처리
        visited = visited.union(graph[curr])

    return len(visited) - 1


number_of_computers = int(input())
number_of_relations = int(input())

relation = {i+1: set() for i in range(number_of_computers)}

for i in range(number_of_relations):
    start, end = map(int, input().split())

    relation[start].add(end)
    relation[end].add(start)

print(bfs(graph=relation, start_point=1))

###################
# memory: 34944KB #
# time:   56ms    #
###################



