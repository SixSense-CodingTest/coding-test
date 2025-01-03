N,r,c = list(map(int,input().split()))


def rec(N,r,c,T):
    print(N,r,c,T)
    if N==1:
        return T + 2*r + c
    
    if r < 2**(N-1) and c < 2**(N-1): # 1 
        return rec(N-1,r,c,T)
    elif r >= 2**(N-1) and c < 2**(N-1): # 2 
        return rec(N-1,r-2**(N-1),c,T+2**(2*N-2))
    elif r < 2**(N-1) and c >= 2**(N-1): # 3 
        return rec(N-1,r,c-2**(N-1),T+2*2**(2*N-2))
    else:
        return rec(N-1,r-2**(N-1),c-2**(N-1),T+3*2**(2*N-2))

print(rec(N,c,r,0))
