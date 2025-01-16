import sys
from heapq import heappop, heappush
input = sys.stdin.readline
n, edge = int(input()), int(input())
graph = [[] for _ in range(n+1)]
for i in range(edge):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

for start in range(1, n+1):
    dist = [10e9] * (n + 1)
    dist[start] = 0
    heap = [(0, start)]

    while heap:
        current_dist, node = heappop(heap)
        if current_dist > dist[node]: continue
        for v, w in graph[node]:
            if current_dist + w < dist[v]:
                dist[v] = current_dist + w
                heappush(heap, (dist[v], v))

    print(*map(lambda x: 0 if x == 10e9 else x, dist[1:]))
# 44724kb
# 2204ms
# 다익스트라 알고리즘 n번 반복 시간 오래걸림

import sys
input = sys.stdin.readline
n, edge = int(input()), int(input())
graph = [[10e8 if i!=j else 0 for i in range(n+1)] for j in range(n+1)]
for i in range(edge):
    u, v, w = map(int, input().split())
    graph[u][v] = min(graph[u][v], w)

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

for i in range(1, n+1):
    print(*map(lambda x: 0 if x == 10e8 else x, graph[i][1:]))
# 33432kb
# 504ms
# 플로이드 알고리즘, i와 j 사이에 임의의 k 노드를 이용 
# i -> j 와 i -> k -> j 를 비교하여 더 낮은 값을 선택

import sys
input = sys.stdin.readline
n, edge = int(input()), int(input())
def solve(n,edge):
    graph = [[10e8 if i!=j else 0 for i in range(n+1)] for j in range(n+1)]
    for i in range(edge):
        u, v, w = map(int, input().split())
        graph[u][v] = min(graph[u][v], w)

    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

    for i in range(1, n+1):
        print(*map(lambda x: 0 if x == 10e8 else x, graph[i][1:]))
solve(n, edge)
# 33432kb
# 228ms
# 종종 다른 사람들 풀이 볼 떄 이렇게 하길래 궁금해서 해봤는데 상당히 빨라짐 신기
# GPT 피셜 글로벌 변수, 로컬 변수 접근할 떄 차이
# 위에서는 graph가 글로벌 변수로 선언되고 아래에서는 로컬변수로 선언되어 더 빠름
# 반복문이 많을 수록 이 차이가 누적되어서 성능 차이가 커진다