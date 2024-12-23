# 듣도 못한 사람의 명단
# 보도 못한 사람의 명단
# 둘다 해당하는 명단 구하기
import sys
from collections import defaultdict

input = sys.stdin.readline

N, M = map(int, input().split())
no_hear_see_dict = defaultdict(int)
name_list = []
count = 0

for _ in range(N):
    no_hear_see_dict[input().strip()] += 1
for _ in range(M):
    no_hear_see_dict[input().strip()] += 1

for key in no_hear_see_dict.keys():
    if no_hear_see_dict[key] > 1:
        name_list.append(key)
        count += 1

name_list.sort()
print(count)
for name in name_list:
    print(name)

## 메모리 45048KB 시간 120ms