# 연결되어 있으면 바이러스 걸림
# 바이러스 걸린 컴퓨터 수 출력
# dict에 저장하고 1번과 연결된 것들을 확인하면서 add하기 
import sys
from collections import defaultdict
input = sys.stdin.readline

N = int(input())
number = int(input())
connect_dict = defaultdict(list)
visited = [0] * (N+1)

for _ in range(number):
    com, connect = map(int, input().split())
    connect_dict[com].append(connect)
    connect_dict[connect].append(com)


def dfs(n):
    visited[n] = 1
    for visit in connect_dict[n]:
        if visited[visit] == 0:
            dfs(visit)
dfs(1)
print(sum(visited)-1)




