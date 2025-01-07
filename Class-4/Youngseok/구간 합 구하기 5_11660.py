import sys
input = sys.stdin.readline
print = sys.stdout.write
n, m = map(int,input().split())
l = [[0] * (n+1)] + [[0]+list(map(int,input().split())) for _ in range(n)]
for i in range(n):
    for j in range(n):
        l[i+1][j+1] += l[i+1][j] + l[i][j+1] - l[i][j]

for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    print(f'{l[x2][y2] - l[x2][y1-1] - l[x1-1][y2] + l[x1-1][y1-1]}\n')
# 73364kb
# 916ms