import sys

input = sys.stdin.readline

T = int(input().strip())

for _ in range(T):
    clothes_dict = {}
    n = int(input().strip())
    for i in range(n):
        clothes, types = map(str, input().split())
        if types in clothes_dict:
            clothes_dict[types].append(clothes)
        else:
            clothes_dict[types] = [clothes]

    result = 1
    for i in clothes_dict:
        result *= len(clothes_dict[i]) + 1

    print(result - 1)

'''
메모리 : 32412KB
시간 : 32 ms
'''
