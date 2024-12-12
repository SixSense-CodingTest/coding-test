import math

N = int(input())
clothes = list(map(int, input().split()))
T, P = map(int, input().split())
T_bundle = 0

for cloth in clothes:
    T_bundle += math.ceil(cloth / T)

P_bundle = N // P
P_remains = N % P

print(T_bundle)
print(P_bundle, P_remains)