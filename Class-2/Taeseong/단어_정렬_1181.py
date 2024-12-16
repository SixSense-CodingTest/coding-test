N = int(input())

words = []
for _ in range(N):
    words.append(input())

print(*sorted(list(set(words)),key=lambda x: (len(x),x)),sep="\n")