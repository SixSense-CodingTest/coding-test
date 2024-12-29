import sys

input = sys.stdin.readline

N, M = map(int, input().split())

poketmon_dict = dict()

for i in range(N):
    poketmon = input().strip()
    poketmon_dict[str(i+1)] = poketmon
    poketmon_dict[poketmon] = str(i+1)

print("\n".join([poketmon_dict[input().strip()] for i in range(M)]))

'''
메모리 : 59712 KB
시간 : 212 ms
'''
