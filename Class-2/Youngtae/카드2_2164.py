# 1 부터 N까지의 번호
# 맨처음엔 버리고 rotate하고

import sys
from collections import deque
input = sys.stdin.readline

N = int(input())

numbers = deque(range(1, N+1))

while len(numbers) != 1:
    numbers.popleft()
    numbers.rotate(-1)

print(numbers[0])
