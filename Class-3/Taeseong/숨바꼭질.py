from collections import deque

N,L = list(map(int,input().split()))

save = set()

Q = deque([[N,0]])

while True:

    x,time = Q.popleft()

    if x == L:
        print(time)
        break 


    if x in save:
        continue
    
    save.add(x)

    if x>0:
        Q.append([x-1,time+1])
    if x*2 <= 100000:
        Q.append([2*x,time+1])
    if x < 100000:
        Q.append([x+1,time+1])

