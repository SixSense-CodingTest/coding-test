import sys
input = sys.stdin.readline
N = int(input().strip())

time_list = list(map(int, input().strip().split()))
time_list.sort()

ans = []
num_sum = 0
for num in time_list:
    num_sum += num
    ans.append(num_sum)
print(sum(ans))

"""
PyPy3
메모리 : 108384 KB
시간 : 96 ms
"""