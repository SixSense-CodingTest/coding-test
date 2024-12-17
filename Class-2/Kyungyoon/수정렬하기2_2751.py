idx_list = [0 for i in range(2000001)]
N = int(input())
for _ in range(N):
    num = int(input())
    idx_list[num + 1000000] = 1

for num, i in enumerate(idx_list):
    if i == 1:
        print(num - 1000000)

# 시간초과
# num_set = set()
# N = int(input())
# for _ in range(N):
#     num = int(input())
#     num_set.add(num)
# sorted_set = sorted(num_set)
# print(*sorted_set, sep='\n')

"""
PyPy3
메모리 : 128264KB
시간 : 688ms

Python3
시간초과
"""