"""
플로이드-워셜 알고리즘
- 그래프에서 모든 쌍의 최단 경로를 효율적으로 계산하는 알고리즘
- 동적 프로그래밍 기법 사용 : 각 정점간 최단거리를 점진적으로 갱신함(간선 하나만 거치는 경로부터 시작해, 점점 더 많은 중간 정점을 거치는 경로까지 고려)
- 가중치가 있는 방향성 그래프에서 작동함
"""
import sys
input = sys.stdin.readline
n = int(input().strip())
m = int(input().strip())

INF = float('inf')

dist = [[INF]*n for _ in range(n)] # dist[i][j] : 노드 i에서 노드 j로 가는 최소 비용

for i in range(n):
    dist[i][i] = 0 # 자기 자신으로 가는 경로의 비용은 0

for i in range(2, 2+m):
    a, b, c = map(int, input().strip().split())
    dist[a-1][b-1] = min(dist[a-1][b-1], c) # dist[a-1][b-1]: 현재 알고있는 a에서 b로 가는 최소비용, c: 새롭게 입력된 a에서 b로 가는 비용

for k in range(n):  # 중간 노드
    for i in range(n):  # 출발 노드
        for j in range(n):  # 도착 노드
            if dist[i][j] > dist[i][k] + dist[k][j]: # 노드 i에서 j로 가는 기존 거리 dist[i][j]와 k를 거쳐가는 거리 dist[i][k]+dist[k][j] 비교해서 더 작은 값 선택
                dist[i][j] = dist[i][k] + dist[k][j]

for i in range(n):
    for j in range(n):
        if dist[i][j] == INF:  # 연결되지 않은 노드
            print(0, end=' ')
        else:
            print(dist[i][j], end=' ')
    print() # 줄바꿈

"""
PyPy3
메모리 : 111692 KB
시간 : 168 ms
"""