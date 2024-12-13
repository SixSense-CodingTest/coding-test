# 점수 중 최댓값 => M
# 모든 점수 => 점수 / M*100 으로 수정
# 수정 후 새로운 평균 내기

def change_score(x,M):
    return x / M * 100

N = int(input())
scores = list(map(int, input().split()))
M = max(scores)
new_sum = 0

for score in scores:
    new_sum += change_score(score, M)

answer = new_sum / N
print(answer)


