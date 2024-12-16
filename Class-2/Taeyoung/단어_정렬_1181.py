import sys

N = int(sys.stdin.readline().strip())

word_dict = {}

for _ in range(N):
    word = sys.stdin.readline().strip()
    word_dict[word] = len(word)

for key, value in sorted(word_dict.items(), key=lambda x: (x[1], x[0])):
    print(key)
