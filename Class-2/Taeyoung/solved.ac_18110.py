import sys
import math
input = sys.stdin.readline


def round(n):
    if n - int(n) >= 0.5:
        return math.ceil(n)
    else:
        return math.floor(n)


N = int(input().strip())

if N == 0:
    print(0)
else:
    score = sorted([int(input().strip()) for _ in range(N)])
    trimmed_mean = round(N*0.15)
    processing_score = score[trimmed_mean:N-trimmed_mean]
    print(round(sum(processing_score) / len(processing_score)))
