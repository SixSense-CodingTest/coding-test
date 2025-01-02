# X 중에 자기보다 작은 서로 다른 좌표의 개수로 변환하기

import sys
input = sys.stdin.readline

N = int(input())
X = list(map(int, input().split()))
X_list = list(set(X))
X_list.sort()
X_dict = {}
for i in range(len(X_list)):
    X_dict[X_list[i]] = i

for i in X:
    print(X_dict[i], end = " ")


#메모리 158288KB , 시간 1928ms