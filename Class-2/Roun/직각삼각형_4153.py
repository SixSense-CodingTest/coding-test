############
# bronze 3 #
############

import sys

input = sys.stdin.readline

temp = list(map(int, input().rstrip().split()))

result = []

while 0 not in temp:
    # 긴 변 탐색을 위한 정렬
    temp = sorted(temp)

    if temp[2]**2 == temp[0]**2 + temp[1]**2:
        result.append("right")
    else:
        result.append("wrong")

    temp = list(map(int, input().rstrip().split()))

print('\n'.join(result))


###################
# memory: 32412KB #
# time:   32ms    #
###################

# 무조건 긴 변이 마지막에 입력된다고 생각해서 틀림