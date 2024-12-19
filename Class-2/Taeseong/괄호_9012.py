N = int(input())

for _ in range(N):
    T = input()
    F = 0 
    for t in T:
        if t == '(':
            F+=1 
        else:
            if F <=0:
                print('NO')
                break 
            else:
                F-=1
    else:
        if F==0:
            print('YES')
        else:
            print('NO')
            