############
# silver 5 #
############

import sys

input = sys.stdin.readline

# version 1
# 그냥 정렬
# num = int(input())
# _list = []

# for i in range(num):
#     _list.append(int(input()))

# _list = map(str, sorted(_list))

# print('\n'.join(_list))

####################
# memory: 132412KB #
# time:   964ms    #
####################

# version 2
# memory 활용해서 최악 시간 2*10**6로 제한
num = int(input())

INT_MAX = 10**6

plus = [False] * (INT_MAX + 1)
minus = [False] * (INT_MAX + 1)

for i in range(num):
    temp = int(input())
    if temp >= 0:
        plus[temp] = True
    else:
        minus[-temp] = True

result = []

for i in range(len(minus) - 1, 0, -1):
    if minus[i]:
        result.append(-i)

for i in range(len(plus)):
    if plus[i]:
        result.append(i)

print('\n'.join(map(str, result)))

####################
# memory: 151636KB #
# time:   916ms    #
####################

