############
# bronze 1 #
############

import sys

def check(target: str):
    left, right = 0, len(target) - 1

    # 가장 왼쪽과 가장 오른쪽부터 쪼여가면서 비교해서 다르면 return "no"
    while left < right:
        if target[left] != target[right]:
            return "no"
        left += 1
        right -= 1
    
    return "yes"
    

input = sys.stdin.readline

ans = []

while True:
    target = input().rstrip()

    if target == '0':
        break

    ans.append(check(target))

print('\n'.join(ans))

###################
# memory: 32412KB #
# time:   32ms    #
###################