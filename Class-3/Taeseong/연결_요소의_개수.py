N, M = list(map(int,input().split()))

graph = [[] for i in range(N+1)]

visited = [False]*(N+1)

for _ in range(M):
    a,b = list(map(int,input().split()))
    graph[a].append(b)
    graph[b].append(a)


stack = list(zip(list(range(1,N+1)),[1]*N))

cnt = 0
while stack:
    # print(stack)
    x,flag = stack.pop()
    
    if visited[x]:
        continue
    
    visited[x] = True
    cnt+=flag
    
    for i in graph[x]:
        if visited[i]:
            continue
        else:
            stack.append([i,0])
    # stack.extend(list(zip(,[0]*len(graph[x]))))


print(cnt)