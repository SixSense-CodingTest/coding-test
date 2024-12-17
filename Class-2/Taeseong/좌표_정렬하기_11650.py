import sys
input = sys.stdin.readline

N = int(input())

dots = []
for i in range(N):
    xi,yi = list(map(int,input().split()))
    dots.append((int(xi),int(yi)))

dots.sort(key=lambda x: (x[0],x[1]))

[print(*dot) for dot in dots]