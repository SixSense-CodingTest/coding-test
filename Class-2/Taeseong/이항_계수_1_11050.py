N,K = list(map(int,input().split()))

def fac(n):

    if n==1 or n==0:
        return 1 
    return n*fac(n-1)


print(int(fac(N)/(fac(N-K)*fac(K))))