# 정점의 개수 N, 간선의 개수 M
# 양 끝점 u, v
# 방향 없는 그래프, 연결 요소의 개수 구하기
# 연결된 거 다 둘러보기 DFS
# 일단 첫번째 정점을 

import sys
from collections import defaultdict
sys.setrecursionlimit(10000)
input = sys.stdin.readline

N, M = map(int, input().split())

connect_dict = defaultdict(list)
visited = [False] * (N+1)

for _ in range(M):
    u, v = map(int, input().split())
    connect_dict[u].append(v)
    connect_dict[v].append(u)


def dfs(start):
    visited[start] = True
    for connect in connect_dict[start]:
        if not visited[connect]:
            dfs(connect)
        
connected_components = 0

for node in range(1, N+1):
    if not visited[node]:
        dfs(node)
        connected_components += 1

print(connected_components)