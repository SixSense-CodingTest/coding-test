"""
이분탐색
- 데이터를 반씩 나누어 탐색 범위를 좁혀가며 원하는 값을 찾는 방식
- 시간 복잡도가 매우 빠르다
- 원리 
    - 탐색범위의 시작점, 끝점 설정
    - 중간 mid 계산
    - mid와 찾고자 하는 값을 비교
"""
N, M = map(int, input().split())
height = list(map(int, input().split()))

low, high = 0, max(height)
res = 0

while low <= high:
    mid = (low + high) // 2
    total = 0

    for h in height:
        if h > mid:
            total += h - mid

    if total >= M:
        res = mid
        low = mid + 1
    else:
        high = mid - 1
print(res)

"""
PyPy3
메모리 : 258492 KB
시간 : 428 ms
"""