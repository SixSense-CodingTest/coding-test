import sys
input = sys.stdin.readline

M = int(input().strip())
# 메모리 초과
# command = [input().strip().split() for _ in range(M)]
S = set()

for _ in range(M):
    # 메모리 초과떠서 for문 안에 선언
    c = input().strip().split()
    cmd = c[0]
    # all, empty 명령어는 2번째 값이 없으므로 에러뜸
    # num = int(c[1])

    if cmd == 'add':
        S.add(int(c[1]))
    elif cmd == 'remove':
        # discard : 요소 없을 때 remove해도 에러 안 뜸
        S.discard(int(c[1]))
    elif cmd == 'check':
        print(0 if int(c[1]) not in S else 1)
    elif cmd == 'toggle':
        S.remove(int(c[1])) if int(c[1]) in S else S.add(int(c[1]))
    elif cmd == 'all':
        # 여기서 int로 값이 들어가므로 c[1]도 int로 바꿔줘야함
        S = set(range(1, 21))
    elif cmd == 'empty':
        S.clear()

"""
PyPy3
메모리 : 127976 KB
시간 : 1828 ms
"""