# 나이와 이름 입력
# 나이 순 정렬, 먼저 가입한 사람 순서로 정렬
import sys
N = int(sys.stdin.readline())
members = []

for i in range(N):
    age, name = sys.stdin.readline().split()
    members.append([int(age),name, i])

members.sort(key= lambda x: [x[0],x[2]])
for age, name, i in members:
    print(age, name)
