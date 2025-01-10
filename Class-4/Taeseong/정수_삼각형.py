N = int(input())

graph = []
for _ in range(N):
    graph.append(list(map(int,input().split())))

save = [[-1]*(len(graph[i])) for i in range(N)]

save[0][0] = graph[0][0]

for i in range(1,N):
    for k in range(len(save[i])):
        comp1 = save[i-1][k-1] if k-1>=0 else -1
        comp2 = save[i-1][k] if k<len(save[i-1]) else -1
        save[i][k] = max(comp1,comp2) + graph[i][k]

print(max(save[-1]))