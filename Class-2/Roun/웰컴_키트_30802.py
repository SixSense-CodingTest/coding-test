############
# bronze 3 #
############

import sys

input = sys.stdin.readline

people = int(input())

t_shirts = list(map(int, input().rstrip().split()))
number_of_t_shirts, number_of_pencils = map(int, input().rstrip().split())

# 1~number_of_t_shirts까지는 1개이므로 -1을 해야함
# 0~number_of_t_shirts-1이면 number_of_t_shirts로 나눌 때 0으로 되므로 +1
stock_of_t_shirts = list(map(lambda x: (x - 1) // number_of_t_shirts + 1, t_shirts))

# print(stock_of_t_shirts)

print(sum(stock_of_t_shirts))
print(people // number_of_pencils, people % number_of_pencils)


###################
# memory: 32412KB #
# time:   32ms    #
###################