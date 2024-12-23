# 번호 별 인출 시간 주어질 때
# 최솟값 조합 구해서 최솟값 출력하기
import sys
input = sys.stdin.readline

N = int(input())
times = list(map(int, input().split()))
wait_time = 0
sum_time = 0
times.sort()

for time in times:
    wait_time += time
    sum_time += wait_time

print(sum_time)


##메모리 32412KB, 시간 36ms