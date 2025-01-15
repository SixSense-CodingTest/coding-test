import sys
input = sys.stdin.readline

N,M = list(map(int,input().strip().split()))

graph = []
# xy = [] 

for i in range(N):
    graph.append(list(map(int,input().strip().split())))


sum_graph = [[0]*(N+1) for i in range(N+1)]

for i in range(1,N+1):
    for k in range(1,N+1):
        sum_graph[i][k] = sum_graph[i-1][k] + sum_graph[i][k-1] - sum_graph[i-1][k-1] + graph[i-1][k-1]


# print(sum_graph)

save = []
for i in range(M):
    x1,y1,x2,y2 = list(map(int,input().strip().split()))
    
    # x1,y1 = x1,y1-1

    res = sum_graph[x2][y2] - sum_graph[x2][y1-1] - sum_graph[x1-1][y2] + sum_graph[x1-1][y1-1] 
    # print(res)
    save.append(str(res))

print('\n'.join(save),end='')