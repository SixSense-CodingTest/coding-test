from collections import defaultdict
N = int(input())
graph = defaultdict(list)
for _ in range(N-1): # 간선개수 N-1
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False]*(N+1)
ans = [0]*(N+1) # 부모 저장 리스트

# 루트노드 방문처리
stack = [1]
visited[1] = True

while stack:
    node = stack.pop()
    for n in graph[node]: # 현재노드와 연결된 노드 모두 확인
        if not visited[n]:
            ans[n] = node # 부모 설정
            visited[n] = True
            stack.append(n)

for i in range(2, N+1):
    print(ans[i])

"""
PyPy3
메모리 : 131692 KB
시간 : 264 ms
"""