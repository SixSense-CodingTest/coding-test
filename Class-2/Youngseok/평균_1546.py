n = int(input())
score = list(map(int,input().split()))
print(100*sum(score)/n/max(score))