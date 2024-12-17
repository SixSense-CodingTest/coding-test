from collections import deque
q = deque(i+1 for i in range(int(input())))
while len(q) > 1:
    q.popleft()
    q.rotate(-1)
print(q.pop())
# 51864kb
# 188ms

import math
n = int(input())
print(2*n-2**(math.ceil(math.log2(n)))) # 2*n에서 n보다 크거나 같은 2의 거듭제곱을 뺀 것
# 34536kb
# 40ms

n, m = int(input()), 1
while n > m : m*=2
print(2*n-m)
# 32412kb
# 44ms

n, m = int(input()), 1
while n > m : m<<=1 # 비트연산자가 더 빠름
print(2*n-m)
# 32412kb
# 36ms