from collections import deque

N = int(input())

save = dict()

done = set()

Q = deque([[N,0]])

while True:

    n,itr = Q.popleft()
    
    if n in done:
        continue
    else:
        done.add(n)

    if n == 1:
        print(itr)
        break

    if n%3==0: Q.append([n//3,itr+1])
    if n%2==0: Q.append([n//2,itr+1])
    Q.append([n-1,itr+1])

    








