"""
좌표압축
- 입력 좌표를 중복없이 정렬해서 좌표의 순서를 구한다
- 정렬된 좌표의 값을 기준으로 각 좌표의 새로운 값을 매핑한다
- 원래의 좌표 배열에서 각 값을 새롭게 매핑된 값으로 변환하여 출력한다
"""
import sys
input = sys.stdin.readline
N = int(input().strip())
num_list = list(map(int, input().strip().split()))

sorted_list = sorted(set(num_list))
num_map = {value:idx for idx, value in enumerate(sorted_list)}
new_list = [num_map[x] for x in num_list]
print(*new_list)

"""
PyPy3
메모리 : 295220 KB
시간 : 848 ms
"""