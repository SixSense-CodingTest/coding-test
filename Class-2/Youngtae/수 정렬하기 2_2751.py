# 첫째 줄 수 N개
# N개의 줄에 오름차순으로 정렬한 결과 출력
import sys

N = int(sys.stdin.readline())
numbers = []
for i in range(N):
    numbers.append(int(sys.stdin.readline()))
numbers.sort()

for number in numbers:
    print(number)


