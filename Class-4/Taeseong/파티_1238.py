import sys
import heapq

input = sys.stdin.readline

N,M,X = list(map(int,input().strip().split()))
# graph = [[1e9]*(N+1) for i in range(N+1)]
graph = [[] for i in range(N+1)]


for _ in range(M):
    s,e,w = list(map(int,input().strip().split()))
    graph[s].append((e,w))


s_to_x = [1e9]*(N+1)
for i in range(1,N+1):
    dp = [1e9]*(N+1)
    Q = [] 
    heapq.heappush(Q,(0,i))

    while Q:
        w,s = heapq.heappop(Q)
        if dp[s]<w:
            continue
        dp[s] = w 
        if s==X:
            s_to_x[i] = w 
            break 
        for ee,ww in graph[s]:
            heapq.heappush(Q,(w+ww,ee))

# x_to_s = [1e9]*(N+1)
x_to_s = [1e9]*(N+1)
Q = [] 
heapq.heappush(Q,(0,X))
while Q:
    w,s = heapq.heappop(Q)
    if x_to_s[s]<w:
        continue
    x_to_s[s] = w 
    for ee,ww in graph[s]:
        heapq.heappush(Q,(w+ww,ee))

max_dist = -1
for i in range(1,N+1):
    if s_to_x[i] + x_to_s[i] > max_dist:
        max_dist = s_to_x[i] + x_to_s[i]

print(max_dist)

# def party(graph):

#     for i in range(1,N+1):
#         for s in range(1,N+1):
#             for e in range(1,N+1):
#                 graph[s][e] = min(graph[s][e],graph[s][i]+graph[i][e])

#     max_dist = -1
#     for i in range(1,N+1):
#         if graph[i][X] + graph[X][i] > max_dist:
#             max_dist = graph[i][X] + graph[X][i]

#     print(max_dist)

# party(graph)

