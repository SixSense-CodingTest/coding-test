N = int(input())
correct = set(map(int, input().split()))
M = int(input())
num_list = list(map(int, input().split()))

for idx in range(len(num_list)):
    if num_list[idx] in correct:
        print(1)
    else: print(0)

"""
PyPy3
메모리 : 145304 KB
시간 : 180 ms
"""