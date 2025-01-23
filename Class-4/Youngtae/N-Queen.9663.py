# N x N 인 체스판 위에 퀸 N개를 서로 공격할 수 없게 놓는 문제
# 퀸 놓는 방법의 수
# 0번째 행의 0번째 열

import sys
input = sys.stdin.readline

N = int(input())

def getAns(N, y, width, diagonal1, diagonal2):
    ans = 0
    if y == N:
        ans += 1
    else:
        for i in range(N):
            if width[i] or diagonal1[i+y] or diagonal2[i-y+N]:
                continue

            width[i] = diagonal1[i+y] = diagonal2[i-y+N] = True 
            ans += getAns(N, y+1, width, diagonal1, diagonal2)

            width[i] = diagonal1[i+y] = diagonal2[i-y+N] = False
    
    return ans

print(getAns(N, 0, [False] * N, [False] * (N*2), [False] * (N*2)))


# call trace 작성
# import sys
# input = sys.stdin.readline

# N = int(input())

# def getAns(N, y, width, diagonal1, diagonal2):
#     ans = 0
#     if y == N:
#         print(f"Reached the end: y={y}, ans={ans+1}")
#         ans += 1
#     else:
#         for i in range(N):
#             print(f"Checking position: y={y}, i={i}, width={width}, diagonal1={diagonal1}, diagonal2={diagonal2}")
#             if width[i] or diagonal1[i+y] or diagonal2[i-y+N]:
#                 print(f"Skipping: y={y}, i={i} (conflict detected)")
#                 continue

#             print(f"Placing queen: y={y}, i={i}")
#             width[i] = diagonal1[i+y] = diagonal2[i-y+N] = True
#             ans += getAns(N, y+1, width, diagonal1, diagonal2)

#             print(f"Removing queen: y={y}, i={i}")
#             width[i] = diagonal1[i+y] = diagonal2[i-y+N] = False
    
#     print(f"Returning: y={y}, ans={ans}")
#     return ans

# print(getAns(N, 0, [False] * N, [False] * (N*2), [False] * (N*2)))


