# 2xn 크기의 직사각형 채우기
# n을 1,2의 조합으로 나타내면 끝 아닐까?
# 2x1의 경우 1개
# 2x2의 경우 1+1, 2 2개
# 2x3 의 경우 1+1+1, 1+2, 2+1 3개
# 2x4 의 경우 1+1+1+1, 1+1+2 * 3,  2+2 5개
# 2x5 의 경우 1+1+1+1+1, 1+1+1+2 *4, 2+1+2 * 3, 8개
# 직전 것 2개의 합인 느낌쓰
import sys

input = sys.stdin.readline

n = int(input())
numbers = [0] * 1001

i = 1
while i != n + 1:
    numbers[1] = 1
    numbers[2] = 2
    if n == 1:
        print(1)
        i += 1
        break
    elif n == 2:
        print(2)
        i += 1
        break
    numbers[i] = numbers[i - 1] + numbers[i - 2]
    i += 1

if n >=3:
    print(numbers[n] % 10007)
