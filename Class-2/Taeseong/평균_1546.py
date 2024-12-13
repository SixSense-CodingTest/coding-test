N = int(input())
Ns = list(map(int,input().split()))

max_ns = max(Ns)

Ns = [i/max_ns*100 for i in Ns]

print(sum(Ns)/len(Ns))