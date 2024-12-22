# N명의 사람
# 순서대로 K번째 사람 제거
# N명이 모두 제거될때까지 반복
# 사람 제거 되는 순서 => print하기
import sys
from collections import deque
input = sys.stdin.readline
N, K = map(int, input().split())

people = deque([i for i in range(1,N+1)])

print("<", end="")
while len(people) != 1:
    people.rotate(-K+1)
    print(people.popleft(), end = ", ")

print(people.popleft(), end ="")
print(">")
    


