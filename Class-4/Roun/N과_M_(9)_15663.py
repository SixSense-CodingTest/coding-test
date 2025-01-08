import sys

def back_tracking(depth: int, used: list):
    global results, result, items, number_of_items, number_of_selections

    if depth == number_of_selections:
        results.append(tuple(result)) 
        return

    for i in range(number_of_items):
        if not used[i]: 
            used[i] = True
            result.append(items[i])
            back_tracking(depth + 1, used)
            result.pop()
            used[i] = False

input = sys.stdin.readline

number_of_items, number_of_selections = map(int, input().split())
items = list(map(int, input().split()))

result = []
results = []
used = [False] * number_of_items

back_tracking(0, used)

# 중복 제거 & 정렬
results = sorted(set(results))

for res in results:
    print(" ".join(map(str, res)))

###################
# memory: 39072KB #
# time:   104ms   #
###################
