n, k = map(int, input().split())
y, p, l = [i+1 for i in range(n)], 0, []
while y: 
    p = (p+k-1)%len(y)
    l.append(str(y.pop(p)))
print(f'<{', '.join(l)}>')
# 32412kb
# 36ms

n, k = map(int, input().split())
y, p, l = [i+1 for i in range(n)], 0, []
while y: 
    p = (p+k-1)%len(y)
    l.append(f'{y.pop(p)}') # f-string이 더 빠른듯
print(f'<{', '.join(l)}>')
# 32412kb
# 32ms 