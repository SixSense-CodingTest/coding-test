n = int(input())
size = map(int, input().split())
t, p = map(int, input().split())
res = 0
for i in size:
    res += (i-1)//t+1
print(res)
print(n//p,n%p)