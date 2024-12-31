import sys

input = sys.stdin.readline

N = int(input().strip())

color_map = [list(map(int, input().split())) for _ in range(N)]

result = []

def cut(x, y, n):    
    color = color_map[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if color != color_map[i][j]:
                cut(x, y, n//2)
                cut(x, y+n//2, n//2)
                cut(x+n//2, y, n//2)
                cut(x+n//2, y+n//2, n//2)
                return
    
    if color == 0:
        result.append(0)
    else:
        result.append(1)

cut(0, 0, N)
print(result.count(0))
print(result.count(1))

'''
메모리 : 32412 KB
시간 : 44 ms
'''