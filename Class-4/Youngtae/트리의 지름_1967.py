# 노드의 개수 n
# 완전탐색
# 1번부터 n번노드까지 자기자신에서 시작해서 노드이동을 해가며 거리기록
# 그중에 최장길이 of 최장 => 트리의 지름

# 시간 초과
import sys
sys = sys.stdin.readline
from collections import deque
from collections import defaultdict

def bfs(node, graph, n):
    visited = [-1] * (n + 1) 
    visited[node] = 0 
    queue = deque([node])
    
    max_distance = 0 
    while queue:
        current = queue.popleft()
        for neighbor, weight in graph[current]:
            if visited[neighbor] == -1:
                visited[neighbor] = visited[current] + weight
                queue.append(neighbor)
                max_distance = max(max_distance, visited[neighbor])

    return max_distance

def tree_diameter(n, edges):
    graph = defaultdict(list)
    for u, v, w in edges:
        graph[u].append((v, w))
        graph[v].append((u, w))

    diameter = 0
    for start_node in range(1, n + 1):
        diameter = max(diameter, bfs(start_node, graph, n))
    
    return diameter

n = int(input())
edges = []
for _ in range(n - 1):
    edges.append(tuple(map(int, input().split())))

print(tree_diameter(n, edges))



import sys
sys = sys.stdin.readline
from collections import defaultdict, deque

def find_farthest_node(start, graph, n):
    visited = [-1] * (n + 1)
    visited[start] = 0
    queue = deque([start])
    
    farthest_node = start
    max_distance = 0
    
    while queue:
        current = queue.popleft()
        for neighbor, weight in graph[current]:
            if visited[neighbor] == -1:
                visited[neighbor] = visited[current] + weight
                queue.append(neighbor)
                if visited[neighbor] > max_distance:
                    max_distance = visited[neighbor]
                    farthest_node = neighbor
    
    return farthest_node, max_distance

def tree_diameter(n, edges):
    graph = defaultdict(list)
    for parent, child, weight in edges:
        graph[parent].append((child, weight))
        graph[child].append((parent, weight))
    
    node_a, _ = find_farthest_node(1, graph, n)
    
    node_b, diameter = find_farthest_node(node_a, graph, n)
    
    return diameter

n = int(input())
edges = []
for _ in range(n - 1):
    edges.append(tuple(map(int, input().split())))

print(tree_diameter(n, edges))
