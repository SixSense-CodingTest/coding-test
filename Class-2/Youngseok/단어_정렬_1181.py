import sys
input = sys.stdin.readline
n = int(input())
words = set([input().strip() for _ in range(n)])
words = sorted(list(words),key = lambda x: (len(x),x))
print('\n'.join(words))