import sys
input = sys.stdin.readline
n = int(input())
s = []
for i in range(n):
    c = input().strip().split()
    if  c[0] == 'push': s.append(c[1])
    elif c[0] == 'pop': print(s.pop() if s else -1)
    elif c[0] == 'size': print(len(s))
    elif c[0] == 'empty': print(0 if s else 1)
    elif c[0] == 'top': print(s[-1] if s else -1)