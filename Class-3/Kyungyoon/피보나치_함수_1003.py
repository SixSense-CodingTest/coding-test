"""
** 배운 내용 **
DP : 큰 문제를 작은 문제로 쪼개서 그 답을 저장해두고 재활용한다.

캐싱이란,
CPU, GPU <- RAM <- SSD, HDD : 데이터가 원래 SSD에 저장돼있는데 걔를 RAM에 올리고, 걔를 CPU, GPU에 올림
이 과정이 오래걸리므로 CPU에 좀 더 가까운 곳에 저장하자
파일 복사본을 캐시 또는 임시 저장하여 보다 빠르게 액세스할 수 있도록 하는 프로세스
"""
memo = {}
def fibonacci(n):
    global memo
    if n in memo:  # 이미 계산된 값이 있으면 반환
        return memo[n]
    if n == 0:
        return [1, 0]
    elif n == 1:
        return [0, 1]
    else:
        fibo_1 = fibonacci(n-1)
        fibo_2 = fibonacci(n-2)
        memo[n] = [fibo_1[0] + fibo_2[0], fibo_1[1] + fibo_2[1]]
        return memo[n]

import sys
input = sys.stdin.readline
T = int(input().strip())

for _ in range(T):
    N = int(input().strip())
    print(*fibonacci(N))

# 시간초과
# zero_one = [0, 0]
# def fibonacci(n):
#     global zero_one
#     if n == 0:
#         zero_one[0] += 1
#         return 0
#     elif n ==1:
#         zero_one[1] += 1
#         return 1
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)

# import sys
# input = sys.stdin.readline
# T = int(input().strip())

# for _ in range(T):
#     zero_one = [0, 0]
#     N = int(input().strip())
#     fibonacci(N)
#     print(*zero_one)

"""
PyPy3
메모리 : 108384 KB
시간 : 92 ms
"""