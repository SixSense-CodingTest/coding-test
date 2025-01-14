"""
DFS(깊이 우선 탐색) : 한 방향으로 깊게 탐색하고 더 탐색할 곳이 없으면 직전에 방문했던 노드로 되돌아가는 방식 
    - LIFO 
    - 스택사용(append, pop)
BFS(너비 우선 탐색) : 현재 노드와 인접한 노드들을 모두 탐색한 후, 다음 깊이로 넘어가는 방식 
    - FIFO 
    - 큐(append, popleft)
    - 최단거리 찾는데 효과적(이동시간 일정한 경우)
다익스트라 알고리즘 : 이동시간이 일정하지 않고, 각 이동 방식에 따라 시간이 다르게 주어지는 경우
    - heapq(우선순위 큐, 최소 힙 : 데이터 중 가장 작은 값, 우선순위가 높은 값 빠르게 꺼내야할 때 유용)
    - heapq.heappop(heap) : 힙에서 최소값 제거 및 반환
    - heapq.heappush() : 힙에 아이템 추가
    - heapq.heapify(list) : 리스트를 힙 구조로 변환
"""
import heapq
from collections import defaultdict

V, E = map(int, input().split())
K = int(input())
u, v, w = map(int, input().split())

graph = defaultdict(list)
graph[u].append((v, w))

for _ in range(E - 1):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

INF = float('inf')

distances = [INF]*(V+1) # 인덱스에 해당하는 정점에서부터 최단거리를 기록할 변수 : distances
distances[K] = 0  # 시작정점거리는 항상 0

pq = [(0, K)]  # (거리,정점)

while pq:
    dist, vertex = heapq.heappop(pq)

    if dist > distances[vertex]: # 이미 더 짧은 경로가 있으면 무시
        continue

    for neighbor, weight in graph[vertex]: # 현재 vertex와 연결된 노드들 확인
        distance = dist + weight # weight를 이동거리라 생각
        if distance < distances[neighbor]:
            distances[neighbor] = distance
            heapq.heappush(pq, (distance, neighbor))

for i in range(1, V + 1):
    print(distances[i] if distances[i] != INF else "INF")

"""
PyPy3
메모리 : 142456 KB
시간 : 484 ms
"""