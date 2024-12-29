"""
DFS(깊이 우선 탐색) : 한 방향으로 깊게 탐색하고 더 탐색할 곳이 없으면 직전에 방문했던 노드로 되돌아가는 방식 - LIFO - 스택사용
BFS(너비 우선 탐색) : 현재 노드와 인접한 노드들을 모두 탐색한 후, 다음 깊이로 넘어가는 방식 - FIFO - 큐
"""

from collections import defaultdict

N, M = map(int, input().split())
graph = defaultdict(list)

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [False]*(N+1) # 0은 사용하지 않음

res = 0 # 연결 요소 개수
for i in range(1, N+1): # 정점번호 1 ~ N까지
    if not visited[i]:
        res += 1
        stack = [i]
        visited[i] = True
        while stack:
            current = stack.pop()
            for neighbor in graph[current]: # 현재 정점에 연결된 모든 인접 정점 확인
                if not visited[neighbor]:
                    visited[neighbor] = True
                    stack.append(neighbor)
print(res)

"""
PyPy3
메모리 : 176876 KB
시간 : 476 ms
"""