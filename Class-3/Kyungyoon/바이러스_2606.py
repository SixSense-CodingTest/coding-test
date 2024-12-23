"""
DFS(깊이 우선 탐색) : 한 방향으로 깊게 탐색하고 더 탐색할 곳이 없으면 직전에 방문했던 노드로 되돌아가는 방식 - LIFO - 스택사용
BFS(너비 우선 탐색) : 현재 노드와 인접한 노드들을 모두 탐색한 후, 다음 깊이로 넘어가는 방식 - FIFO - 큐
"""
N = int(input())
M = int(input())

# 그래프 초기화
graph = {i: [] for i in range(1, N+1)} 

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 방문 여부 체크
visited = [False] * (N+1)
# 현재 위치 저장
stack = [1]
# 현재 노드 방문처리
visited[1] = True

while stack:
    current = stack.pop()
    for node in graph[current]:
        if not visited[node]:
            visited[node] = True
            stack.append(node)

print(sum(visited) - 1)

"""
PyPy3
메모리 : 108384 KB
시간 : 92 ms
"""