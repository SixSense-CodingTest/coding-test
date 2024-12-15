def fac(a):
    res = 1
    for i in range(a):
        res*=i+1
    return res

n,r = map(int,input().split())
print(fac(n)//(fac(r)*fac(n-r)))