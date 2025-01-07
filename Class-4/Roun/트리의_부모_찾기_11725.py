############
# silver 2 #
############

import sys
from collections import deque

def get_parents(graph: dict) -> dict:
    queue = deque([1])
    visited = set([1])
    result = {}

    while queue:
        curr = queue.popleft()
        
        for node in graph[curr]:
            if node not in visited:
                result[node] = curr
                queue.append(node)
                visited.add(node)

    return result


input = sys.stdin.readline

number_of_nodes = int(input())
graph = {}

graph[1] = set()

for _ in range(number_of_nodes - 1):
    node1, node2 = map(int, input().split())

    graph.setdefault(node1, set()).add(node2)
    graph.setdefault(node2, set()).add(node1)

ans = get_parents(graph)

for node in sorted(ans.keys()):
    print(ans[node])


###################
# memory: 86552KB #
# time:   508ms   #
###################