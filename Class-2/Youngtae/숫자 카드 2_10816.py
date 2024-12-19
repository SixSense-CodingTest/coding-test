# 숫자 카드 N개
import sys
from collections import defaultdict

input = sys.stdin.readline

N = int(input())
numbers = list(map(int, input().split()))
count_num = defaultdict(int)
for number in numbers:
    count_num[number] += 1

M = int(input())
jungsus = list(map(int, input().split()))

for jungsu in jungsus:
    print(count_num[jungsu], end = " ")
        
    
