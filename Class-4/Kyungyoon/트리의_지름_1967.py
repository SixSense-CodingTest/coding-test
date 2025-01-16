import sys
input = sys.stdin.readline
n = int(input().strip())

from collections import defaultdict
tree = defaultdict(list)
for _ in range(n-1):
    parent, child, weight = map(int, input().split())
    tree[parent].append((child, weight))
    tree[child].append((parent, weight))

# 루트 노드에서 가장 먼 노드 찾기 : 지름의 한쪽 끝점
distances = [-1] * (n + 1)
distances[1] = 0

stack = [(1, 0)]  # (루트노드, 현재 거리)
while stack:
    node, distance = stack.pop()
    for neighbor, weight in tree[node]:
        if distances[neighbor] == -1:
            distances[neighbor] = distance + weight
            stack.append((neighbor, distances[neighbor]))

start = distances.index(max(distances))

# 가장 먼 노드에서 다시 DFS 수행 : 지름의 반대쪽 끝점
distances = [-1] * (n + 1)
distances[start] = 0

stack = [(start, 0)] 
while stack:
    node, distance = stack.pop()
    for neighbor, weight in tree[node]:
        if distances[neighbor] == -1:
            distances[neighbor] = distance + weight
            stack.append((neighbor, distances[neighbor]))

print(max(distances))

"""
PyPy3
메모리 : 115272 KB
시간 : 140 ms
"""