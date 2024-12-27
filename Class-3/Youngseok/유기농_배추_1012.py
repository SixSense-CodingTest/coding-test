import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
def dfs(x,y,d):
    del d[(x,y)]
    for dx, dy in [(0,1),(0,-1),(1,0),(-1,0)]:
        nx, ny = x+dx, y+dy
        if (nx, ny) in d: dfs(nx,ny,d)
for _ in range(int(input())):
    w, h, k = map(int, input().split())
    d = {tuple(map(int, input().split())): 1 for _ in range(k)}
    r = 0
    while d:
        dfs(*list(d.keys())[0],d)
        r += 1
    print(r)
# 33864kb
# 48ms