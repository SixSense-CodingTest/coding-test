"""
마을 개수 : N = 학생 수
파티 일어나는 마을 : X번째 마을
단방향 도로 개수 : M
i번째 길을 지나는데 걸리는 시간 : Ti
조건 1 : 파티에 참석했다가 다시 본인 마을로 돌아와야 한다
조건 2 : 최단 시간에 오고가기를 원한다
조건 3 : 단방향 도로여서 오고 가는 길이 다를지도 모른다
조건 4 : 시작점과 끝점이 같은 도로는 없다
출력 : N명의 학생 중 오고 가는데 가장 많이 시간 소비한 학생의 소요시간

다익스트라 알고리즘 : 이동시간이 일정하지 않고, 각 이동 방식에 따라 시간이 다르게 주어지는 경우
    - heapq(우선순위 큐, 최소 힙 : 데이터 중 가장 작은 값, 우선순위가 높은 값 빠르게 꺼내야할 때 유용)
    - heapq.heappop(heap) : 힙에서 최소값 제거 및 반환
    - heapq.heappush() : 힙에 아이템 추가
    - heapq.heapify(list) : 리스트를 힙 구조로 변환
"""
import sys
import heapq
input = sys.stdin.readline
N, M, X = map(int, input().strip().split())

INF = float('inf')

graph = [[] for _ in range(N+1)] # 일반 방향
reverse_graph = [[] for _ in range(N+1)] # 역방향

for _ in range(M):
    start, end, t = map(int, input().strip().split())
    graph[start].append((end, t))
    reverse_graph[end].append((start, t))

def find_dist(start, graph):
    distance = [INF]*(N+1)
    distance[start] = 0
    pq = [(0, start)]  #(소요시간,노드)
    while pq:
        current_time, current_node = heapq.heappop(pq)
        if current_time > distance[current_node]:
            continue
        for next_node, time in graph[current_node]:
            new_time = current_time+time
            if new_time < distance[next_node]:
                distance[next_node] = new_time
                heapq.heappush(pq, (new_time, next_node))
    return distance # 시작노드에서 각 노드까지 최단거리 기록됨

# 시작노드 X : X에서 각 노드로 가는 최단거리
to_party = find_dist(X, graph)

# 시작노드 X : 각 노드에서 X로 오는 최단거리
from_party = find_dist(X, reverse_graph)

max_time = 0
for i in range(1, N + 1):
    max_time = max(max_time, to_party[i]+from_party[i])
print(max_time)

"""
graph = [
    [],          # 0번 노드는 사용하지 않음
    [(2, 4)],    # 1번 노드 → 2번 노드로 가는 데 4의 시간이 걸림
    [(3, 3)],    # 2번 노드 → 3번 노드로 가는 데 3의 시간이 걸림
    [(4, 2)],    # 3번 노드 → 4번 노드로 가는 데 2의 시간이 걸림
    []           # 4번 노드는 다른 노드로 가지 않음
]

reverse_graph = [
    [],          # 0번 노드는 사용하지 않음
    [],          # 1번 노드로 들어오는 경로가 없음
    [(1, 4)],    # 2번 노드 ← 1번 노드로 가는 데 4의 시간이 걸림
    [(2, 3)],    # 3번 노드 ← 2번 노드로 가는 데 3의 시간이 걸림
    [(3, 2)]     # 4번 노드 ← 3번 노드로 가는 데 2의 시간이 걸림
]
"""

"""
PyPy3
메모리 : 111932 KB
시간 : 152 ms
"""