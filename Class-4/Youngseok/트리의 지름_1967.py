import sys
input = sys.stdin.readline
n = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    parent, child, weight = map(int, input().split())
    graph[parent].append((child, weight))
    graph[child].append((parent, weight))

def maxdist(start):
    distance = [-1] * (n+1)
    distance[start] = 0
    q = [start]
    while q:
        node = q.pop()
        for neighbor, weight in graph[node]:
            if distance[neighbor] == -1:
                distance[neighbor] = distance[node] + weight
                q.append(neighbor)
    max_dist = max(distance)
    max_idx = distance.index(max_dist)
    return max_dist, max_idx

print(maxdist(maxdist(1)[1])[0])
# 35480kb
# 56ms