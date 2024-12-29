import sys

input = sys.stdin.readline

N, M = map(int, input().split())

address_passwd_map = dict(map(str, input().split()) for _ in range(N))
find_passwd = [address_passwd_map[input().strip()] for _ in range(M)]

print("\n".join(find_passwd))

'''
메모리 : 51480 KB
시간 : 176 ms
'''
