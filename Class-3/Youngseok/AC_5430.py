from collections import deque
for _ in range(int(input())):
    c, n = input(), int(input())
    l = deque(input().strip('[]').split(','))
    if c.count('D') > n: 
        print('error')
        continue
    f = False
    for i in c:
        if i == 'R': f = not f
        elif l: 
            if f: l.pop()
            else: l.popleft()
    if f: l.reverse()
    print(f'[{','.join(l)}]')
# 41064kb
# 152ms

for _ in range(int(input())):
    c, n = input().split('R'), int(input())
    l = input().strip('[]').split(',')
    st, ed = len(''.join(c[::2])), n-len(''.join(c[1::2]))
    if st-ed > n+1: print('error')
    else: 
        l = l[st:ed]
        print(f'[{','.join(l if len(c)%2 else reversed(l))}]')
# 41268kb
# 76ms