from collections import deque

M,N = list(map(int,input().split()))

box = []

ripen = []

for y in range(N):
    row = list(map(int,input().split()))
    box.append(row)
    for x in range(len(row)):
        if row[x]==1:
            ripen.append([y,x,0])

Q = deque(ripen)

while Q:

    y,x,time = Q.popleft()    
    
    for dy,dx in zip([1,-1,0,0],[0,0,1,-1]):
        py,px = y+dy,x+dx
        
        if py<0 or py>=N or px<0 or px>=M:
            continue

        if box[py][px] == -1 or box[py][px]==1:
            continue

        box[py][px] = 1 

        Q.append([py,px,time+1])

for row in box:
    if 0 in row:
        print(-1)
        break 
else: 
    print(time)
