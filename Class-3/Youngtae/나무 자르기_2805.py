# H 보다 큰 나무는 위에 부분이 잘림
# 잘린 위에부분을 집으로 들고감
# M 미터를 가져가는 최대 H높이 구하기
# 초기 설정값은 나무 최대높이값으로 설정
# 그렇게 나무를 자르다가 M 값이 나오면 출력 하는 식


# 1번 방안 => 시간 초과
# import sys
# input = sys.stdin.readline

# N, M = map(int, input().split())
# wood_heights = list(map(int, input().split()))

# max_height = max(wood_heights)
# while True:
#     wood_take = sum([wood_height - max_height for wood_height in wood_heights if wood_height > max_height])
#     if wood_take == M:
#         break
#     max_height -= 1

# print(max_height)

# 이진 탐색
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
wood_heights = list(map(int, input().split()))

low, high = 0, max(wood_heights)
result = 0

while low <= high:
    mid = (low+high) // 2

    wood_taken = sum([wood_height - mid for wood_height in wood_heights if wood_height > mid])
    if wood_taken >= M:
        result = mid
        low = mid + 1
    else:
        high = mid - 1

print(result)