import sys
input = sys.stdin.readline
def dfs(map, c):
    l, s = len(map), sum(sum(row) for row in map)
    if s == l*l: c[1] += 1
    elif s == 0: c[0] += 1
    else:
        l //= 2
        for i in range(0,2*l,l):
            for j in range(2):
                nmap = [map[k][i:i+l] for k in range(j*l, (j+1)*l)]
                dfs(nmap, c)
p = [list(map(int,input().split())) for _ in range(int(input()))]
c = [0, 0]
dfs(p, c)
for i in c: print(i)
# 32412kb
# 52ms