import sys
input = sys.stdin.readline
n = int(input())
s = set()
for i in range(n):
    c = input().strip().split()
    if c[0] == 'add': s.add(c[1])
    elif c[0] == 'remove': s.discard(c[1])
    elif c[0] == 'check': print(1 if c[1] in s else 0)
    elif c[0] == 'toggle': s.discard(c[1]) if c[1] in s else s.add(c[1])
    elif c[0] == 'all': s = set(['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20'])
    elif c[0] == 'empty': s = set()