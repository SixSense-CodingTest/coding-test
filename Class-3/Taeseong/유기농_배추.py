
T = int(input())

dy = [1,-1,0,0]
dx = [0,0,1,-1]

dxy = [[1,0],[],[],[]] 

for _ in range(T):
    
    M,N,K = list(map(int,input().split()))
    field = [[0]*M for _ in range(N)]

    res = 0 
    stack = []

    for i in range(K):
        x,y = list(map(int,input().split()))
        field[y][x] = 1 
        stack.append([y,x,1])
    
    while stack:
        # print(stack)
        y,x,seen = stack.pop()

        if y>=N or y<0 or x>=M or x<0 or field[y][x] == 0:
            # break
            continue
        
        field[y][x] = 0
        res += seen

        for ddy,ddx in zip(dy,dx):
            py,px = y+ddy,x+ddx

            stack.append([py,px,0])

    print(res)






