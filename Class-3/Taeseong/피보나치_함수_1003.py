cache = {0:[1,0],1:[0,1]}

def fibo(n):
    
    if n in cache.keys():
        return cache[n]
    
    zo1 = fibo(n-1)
    zo2 = fibo(n-2)
    cache[n] = [zo1[0]+zo2[0],zo1[1]+zo2[1]]

    return cache[n]

T = int(input())

for _ in range(T):

    N = int(input())
    print(*fibo(N))