N, r, c = map(int, input().split())

result = 0

# Z모양 탐색
while N > 0:
    N -= 1
    half = 2 ** N # 현재 배열 한 변의 절반
    area = half * half # 한 사분면 크기

    # 현재 위치가 어느 사분면에 속하는지 판단
    if r < half and c < half: # 1사분면
        pass # 탐색 순서의 시작점이라서 pass
    elif r < half and c >= half: # 2사분면
        result += area
        c -= half # 열 인덱스를 2 사분면 기준으로 조정(해당 사분면의 기준점 재조정)
    elif r >= half and c < half:  # 3사분면
        result += 2 * area
        r -= half  # 행 인덱스를 3 사분면 기준으로 조정(해당 사분면의 기준점 재조정)
    else:  # 4사분면
        result += 3 * area
        r -= half
        c -= half
print(result)

"""
PyPy3
메모리 : 108384 KB
시간 : 92 ms
"""