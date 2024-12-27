n = int(input())
c = set([666]+[int(str(i)[:j]+'666'+str(i)[j:]) for i in range(2800) for j in range(len(str(i))+1)])
for i in range(100): c.add(int('6660'+str(i)))
for i in range(10): c.add(int('66600'+str(i)))
c = sorted(list(c))
print(c[n-1])

n = int(input())
c, i = 0, 0
while c != n:
    six, tmp = 1, i
    while tmp % 10 == 6:
        six *= 10
        tmp //= 10
        
    for j in range(six):
        t = i*1000 + 666//six*six + j
        c += 1
        if c == n: break
    i += 1
print(t)