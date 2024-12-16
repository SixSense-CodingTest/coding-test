def gcd(a,b):
    while b: 
        a, b = b, a%b
    return a

def lcm(a,b):
    d = gcd(a,b)
    return a*b//d

a,b = map(int,input().split())
print(gcd(a,b),lcm(a,b))