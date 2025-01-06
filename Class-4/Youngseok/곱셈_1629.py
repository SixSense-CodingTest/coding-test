a,b,c = map(int, input().split())
l = [a]
for i in range(31): l.append(l[i]**2%c)
b = f'{b:b}'[::-1]
r = 1
for i in range(len(b)): 
    if b[i] == '1': r = r*l[i]%c
print(r)
# 32412kb
# 32ms

a,b,c = map(int, input().split())
r = 1
while b:
    if b%2: r = r*a%c
    a = a*a%c
    b //= 2
print(r)
# 32544kb
# 32ms
