from collections import defaultdict
card_D = defaultdict(int)

N = int(input())
card = list(map(int, input().split()))
M = int(input())
check = list(map(int, input().split()))

for c in card:
    card_D[c] += 1

ans = [0] * M
for idx, c in enumerate(check):
    if c in card_D.keys():
        ans[idx] = card_D[c]
print(*ans)

# 시간초과
# N = int(input())
# card = list(map(int, input().split()))
# M = int(input())
# check = list(map(int, input().split()))

# ans = [0] * M
# for c in card:
#     if c in check:
#         ans[check.index(c)] += 1
# print(*ans)

"""
PyPy3
메모리 : 261184 KB
시간 : 540 ms
"""