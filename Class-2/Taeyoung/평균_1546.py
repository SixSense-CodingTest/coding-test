import sys

N = int(sys.stdin.readline())

scores = list(map(int, sys.stdin.readline().split()))

new_scores = [i/max(scores)*100 for i in scores]

print(sum(new_scores)/len(new_scores))