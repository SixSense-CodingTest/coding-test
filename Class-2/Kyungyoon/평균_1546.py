N = int(input())
score = list(map(int, input().split()))
max_score = max(score)
score = [(sco / max_score) * 100 for sco in score]
print(sum(score)/len(score))