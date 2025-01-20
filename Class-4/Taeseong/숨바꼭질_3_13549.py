import heapq

N,K = list(map(int,input().split()))

Q = []
heapq.heappush(Q,(0,N))

visited = [int(1e9)]*(100001) 
visited[N] = 0

while Q:
    time,cur_x = heapq.heappop(Q)

    for dx in (cur_x+1,cur_x-1,cur_x*2):
        if dx < 0 or dx>100000:
            continue

        dt = time 
        if dx != cur_x*2:
            dt = time+1

        if visited[dx] > dt:
            visited[dx] = dt
            heapq.heappush(Q,(dt,dx))


print(visited[K])
