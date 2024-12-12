N = int(input())
S = list(map(int, input().split()))
T, P = map(int, input().split())

ans1 = 0
for s in S:
  ans1 += (s + T - 1) // T

ans2 = N // P
ans3 = N % P

print(ans1)
print(ans2, ans3)