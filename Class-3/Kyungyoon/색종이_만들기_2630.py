N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]

white = 0
blue = 0

def check(input_list):
    global white, blue
    flag = input_list[0][0]
    for row in input_list:
        for i in row:
            if flag == i:
                continue
            else: 
                return False
    if flag == 1:
        blue += 1
    else:
        white += 1
    return True

stack = []
stack.append(paper)

while stack:
    element = stack.pop()
    res = check(element)
    if res:
        continue
    else:
        stack.append([row[:len(element)//2] for row in element[:len(element)//2]]) # 1
        stack.append([row[len(element)//2:] for row in element[:len(element)//2]]) # 2
        stack.append([row[:len(element)//2] for row in element[len(element)//2:]]) # 3
        stack.append([row[len(element)//2:] for row in element[len(element)//2:]]) # 4

print(white)
print(blue)

"""
PyPy3
메모리 : 112176 KB
시간 : 124 ms
"""