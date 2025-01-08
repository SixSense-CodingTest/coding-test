# 트리 만들고 부모 노드 출력하기

import sys
from collections import defaultdict
from collections import deque

input = sys.stdin.readline

N = int(input()) # 노드 개수
tree = defaultdict(list)

for _ in range(N-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

queue = deque()
visited = [False] * (N+1)
visited[1] = True
parents = [0] * (N+1)
queue.append(1)
while queue:
    now = queue.popleft()
    for neighbor in tree[now]:
        if not visited[neighbor]:
            parents[neighbor] = now
            visited[neighbor] = True
            queue.append(neighbor)

for parent in parents[2:]:
    print(parent)
