from collections import deque
import sys

input = sys.stdin.readline

N, K = map(int, input().split())
visited = [0] * 100001


def bfs():
    q = deque([N])

    while q:
        c = q.popleft()

        if c == K:
            return visited[c]

        for cx in [c+1, c-1, 2*c]:
            if 0 <= cx <= 100000 and visited[cx] == 0:
                q.append(cx)
                visited[cx] = visited[c] + 1


print(bfs())
'''
메모리 : 38148KB
시간 : 92ms
'''
