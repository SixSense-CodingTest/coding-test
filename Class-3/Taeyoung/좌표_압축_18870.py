import sys

input = sys.stdin.readline

N = int(input().strip())
num_list = list(map(int, input().split()))

num_dict = {value:idx for idx, value in enumerate(sorted(set(num_list)))}

print(" ".join(map(str, [num_dict[i] for i in num_list])))

'''
메모리 : 186208KB
시간 : 1512ms
'''