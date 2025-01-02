N = int(input())
meetings = [tuple(map(int, input().split())) for _ in range(N)]

# 겹치지 않으면서 최대한 많은 회의를 선택하기 위해 끝나는 시간 기준으로 정렬
meetings.sort(key= lambda x: (x[1], x[0]))
cnt = 0
last_end = 0
for start, end in meetings:
    if start >= last_end: # 겹치지 않음
        cnt += 1
        last_end = end
print(cnt)

"""
PyPy3
메모리 : 126020 KB
시간 : 432 ms
"""