import sys

input = sys.stdin.readline

N = input()
N_list = set(map(int, input().split()))

M = input()

print("\n".join(['1' if i in N_list else '0' for i in list(map(int, input().split()))]))

####################
# memory: 52416KB  #
# time:   108ms    #
####################