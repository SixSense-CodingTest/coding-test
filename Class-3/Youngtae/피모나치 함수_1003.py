# 첫째줄 테스트 케이스 개수 T
# 각 줄엔 N값 주어짐
# fin(0), fin(1) 출력 횟수 구하기
import sys
input = sys.stdin.readline

memory = [[0,0] for _ in range(41)]
memory[0] = [1,0]
memory[1] = [0,1]

for i in range(2,41):
    memory[i][0] = memory[i-1][0] + memory[i-2][0]  
    memory[i][1] = memory[i-1][1] + memory[i-2][1]  

T = int(input())
results = []
for _ in range(T):
    N = int(input())
    print(memory[N][0], memory[N][1])


## 메모리 32412KB 시간 36ms