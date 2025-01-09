############
# silver 1 #
############

import sys

def solve(target: int, times: int) -> int:
    global modular

    # print(f"target: {target}, times: {times}")
    # times: 11 -> 5 -> 2 -> 1

    target %= modular

    if times == 1:
        return target
    
    # 짝수라면, times를 절반으로 나누고, target은 제곱
    if times % 2 == 0:
        return solve(target ** 2, times // 2)
    # 홀수라면, 짝수처럼 하되, target이 1개 남으므로 곱해주고 modular로 나눠줌
    else:
        return (target * solve((target ** 2) % modular, times // 2)) % modular

input = sys.stdin.readline

target, times, modular = map(int, input().split())

# print(target ** times % modular)
# (target * target * ... * target) % modular
# (target % modular * target % modular * ... * target % modular) % modular # times == 11

print(solve(target, times))

###################
# memory: 32412KB #
# time:   36ms    #
###################