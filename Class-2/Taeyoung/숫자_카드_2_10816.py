import sys
from collections import Counter

input = sys.stdin.readline

N = int(input())
cards = Counter(list(map(int, input().split())))

M = int(input())
print(" ".join([str(cards[i]) if i in cards else '0' for i in list(map(int, input().split()))]))

'''
메모리 : 124956 KB
시간 : 552 ms
'''