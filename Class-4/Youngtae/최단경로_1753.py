# 정점의 개수 V, 간선의 개수 E
# 시작정점의 번호 V
# E개의 줄에 걸쳐 각 간선 u,v,w가 주어짐
# 서로 다른 두 정점에 여러 개의 간선 존재할 수 있음
# 일단 각 정점 별로 연결된 정점, 간선의 길이 저장
# 시작점 기준으로 간선의 길이가 최소인 값을 고르기
# 거리가 INF로 초기화 해놓고 

import sys
import heapq
from collections import defaultdict

input = sys.stdin.readline
INF = float('inf')

V, E = map(int, input().split())
K = int(input())
graph = defaultdict(list)

visited = [-1] * (V + 1) 

for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

def dijkstra(start):
    
    distance = [INF] * (V + 1)
    distance[start] = 0
    
    # 우선순위 큐 초기화
    pq = []
    heapq.heappush(pq, (0, start))  # (거리, 정점)
    
    while pq:
        current_dist, current_node = heapq.heappop(pq)
        
        if current_dist > distance[current_node]:
            continue
        
        for neighbor, weight in graph[current_node]:
            new_dist = current_dist + weight
            
            if new_dist < distance[neighbor]:
                distance[neighbor] = new_dist
                heapq.heappush(pq, (new_dist, neighbor))
    
    return distance

shortest_distances = dijkstra(K)

for i in range(1, V + 1):
    if shortest_distances[i] == INF:
        print("INF")
    else:
        print(shortest_distances[i])



