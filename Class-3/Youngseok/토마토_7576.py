n, m = map(int,input().split())
box = [[-1]*(n+2)]+[[-1]+list(map(int,input().split()))+[-1] for _ in range(m)]+[[-1]*(n+2)]
s = []
for i in range(1, n+1):
    for j in range(1, m+1):
        if box[j][i] == 1: s.append((i, j))  
c = -1
while s:
    ns = []
    for x, y in s:
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nx, ny = x+dx, y+dy
            if box[ny][nx] == 0:
                box[ny][nx] = 1
                ns.append((nx, ny))
    c += 1
    s = ns
for i in range(1, n+1):
    for j in range(1, m+1):
        if box[j][i] == 0: break
    else: continue
    print(-1)
    break
else: print(c)
# 146788kb
# 1592ms