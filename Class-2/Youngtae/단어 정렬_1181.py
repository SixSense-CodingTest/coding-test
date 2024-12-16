# N개의 단어가 들어오면 정렬하는 프로그램 작성
# 길이 짧은 순
# 길이 같으면 사전 순
words = []

N = int(input())
for i in range(N):
    words.append(input())

sorted_words = sorted(list(set(words)), key = lambda x: [len(x), x])

for word in sorted_words:
    print(word)
