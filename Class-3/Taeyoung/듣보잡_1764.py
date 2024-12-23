import sys

input = sys.stdin.readline

N, M = map(int, input().split())

dont_hear = set(input().strip() for _ in range(N))
dont_see = set(input().strip() for _ in range(M))

result = sorted(dont_hear & dont_see)

print(len(result))
print("\n".join(i for i in result))

'''
메모리 : 43168 KB
시간 : 76 ms
'''
