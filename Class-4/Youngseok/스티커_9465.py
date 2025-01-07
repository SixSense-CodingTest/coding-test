import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n = int(input())
    u = list(map(int,input().split()))
    d = list(map(int,input().split()))
    v = [0, 0, 0, 0]
    for i in range(n):
        tmp1, tmp2 = v[0], v[1]
        v[0], v[1] = max(v[1], v[3]) + u[i], max(v[0], v[2]) + d[i]
        v[2], v[3] = tmp1, tmp2
    print(max(v))
# 41012kb
# 576ms