from collections import defaultdict
n, d = input(), defaultdict(int)
for i in input().split(): d[i] += 1
m = input()
print(" ".join(map(str, (d[i] for i in input().split()))))
# 155876kb
# 608ms