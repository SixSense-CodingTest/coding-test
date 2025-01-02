n, m = map(int, input().split())
l = [input().split() for _ in range(n)]
for i in range(n):
    for j in range(m): 
        if l[i][j] == '2': break
    else: continue
    break
r = [['-1' if l[i][j] == '1' else '0' for j in range(m)] for i in range(n)]
c, nn = 1, [(i, j)]
while nn:
    tn = []
    while nn:
        x, y = nn.pop()
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nx, ny = x + dx, y + dy
            if nx < 0 or ny < 0 or nx > n-1 or ny > m-1: continue
            if r[nx][ny] == '-1':
                r[nx][ny] = f'{c}'
                tn.append((nx, ny))
  
    nn = tn
    c += 1
for i in r: print(' '.join(i))
# 48000kb
# 584ms

n, m = map(int, input().split())
l = [input().split() for _ in range(n)]
c, nn = 1, []
for i in range(n):
    for j in range(m): 
        if l[i][j] == '1': l[i][j] = '-1'
        elif l[i][j] == '2': 
            nn.append((i, j))
            l[i][j] = '0'
while nn:
    tn = []
    while nn:
        x, y = nn.pop()
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nx, ny = x + dx, y + dy
            if nx < 0 or ny < 0 or nx > n-1 or ny > m-1: continue
            if l[nx][ny] == '-1':
                l[nx][ny] = f'{c}'
                tn.append((nx, ny))
  
    nn = tn
    c += 1
for i in l: print(' '.join(i))
# 45884kb
# 600ms

n, m = map(int, input().split())
l = [input().replace('1', '-1').split() for _ in range(n)]
for i in range(n):
    for j in range(m): 
        if l[i][j] == '2': 
            l[i][j] = '0'
            break
    else: continue
    break
c, nn = 1, [(i, j)]
while nn:
    tn = []
    while nn:
        x, y = nn.pop()
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nx, ny = x + dx, y + dy
            if nx < 0 or ny < 0 or nx > n-1 or ny > m-1: continue
            if l[nx][ny] == '-1':
                l[nx][ny] = f'{c}'
                tn.append((nx, ny))
  
    nn = tn
    c += 1
for i in l: print(' '.join(i))
# 45884kb
# 584ms