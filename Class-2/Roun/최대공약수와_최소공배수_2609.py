############
# bronze 1 #
############

import sys

input = sys.stdin.readline

num1, num2 = map(int, input().rstrip().split())

max_divisor = 1

for i in range(1, min(num1, num2) + 1):
    if num1 % i == 0 and num2 % i == 0:
        max_divisor = i

print(max_divisor)
print(max_divisor * num1 // max_divisor * num2 // max_divisor)

###################
# memory: 32412KB #
# time:   36ms    #
###################