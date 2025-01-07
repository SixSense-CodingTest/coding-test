"""
분할 정복 : 큰 문제를 더 작은 하위 문제로 나누기
기본 아이디어
- 큰 수를 곱한 후 나머지 구하는 것 = 각각의 수의 나머지를 구해 곱한 후 나머지를 구하는 것
- B가 홀수일 때 : A^{B} = A * A^{B-1}
- B가 짝수일 때 : A^{B} = (A^{B/2})^{2}
"""
import sys
input = sys.stdin.readline
A, B, C = map(int, input().strip().split())

result = 1
base = A % C

while B > 0: # 지수가 0이 될 때까지
    if B % 2 == 1:
        result = (result * base) % C # A^{B} = A * A^{B-1}에서 A 처리
    base = (base * base) % C # 짝수 지수 처리
    B //= 2 

print(result)

"""
PyPy3
메모리 : 108384 KB
시간 : 96 ms
"""