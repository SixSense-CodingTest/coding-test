from collections import deque

N,M = list(map(int,input().split()))

graph = []
dist = [[-1]*M for i in range(N)]

dx = [1,-1,0,0]
dy = [0,0,1,-1]

tmp = None
for i in range(N):
    row = list(map(int,input().split()))
    graph.append(row)
    for k in range(M):
        if row[k] == 2:
            tmp = [i,k]
        if row[k] == 0:
            dist[i][k] = 0 
        



Q = deque([[tmp[0],tmp[1],0]])

while Q:
    y,x,d = Q.popleft()

    if y<0 or y>=N or x<0 or x>=M:
        continue

    if dist[y][x] != -1:
        continue

    # if graph[y][x] == 0:
    #     dist[y][x] = 0
    #     continue

    dist[y][x] = d 

    for ddy,ddx in zip(dy,dx):
        py,px = y+ddy,x+ddx
        
        Q.append([py,px,d+1])



for i in dist:
    print(*i)