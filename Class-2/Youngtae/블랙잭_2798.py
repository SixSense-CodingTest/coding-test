# M을 넘지않으면서 3개로 최대한 가까운 3장의 합 출력하기
# 첫줄 N 카드개수, 제한 수 M 주어짐
# 두번째줄 카드 뭐 쓰여있는지 N개 주어짐
# 최종 3장의 합 출력하기
# 오름차순으로 정렬하고 3개
from itertools import permutations

N, M = map(int, input().split())
numbers = list(map(int, input().split()))
max_num = 0

for permutation in permutations(numbers,3):
    if sum(permutation) <= M:
        if sum(permutation) > max_num:
            max_num = sum(permutation)

print(max_num)



