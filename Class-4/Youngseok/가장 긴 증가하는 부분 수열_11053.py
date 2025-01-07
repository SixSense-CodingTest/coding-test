n = int(input())
l = {0:0}
for i in map(int, input().split()):
    for j in list(l.keys()):
        if j < i : 
            if i in l and l[i] > l[j]: continue
            l[i] = l[j]+1
print(max(l.values()))
# 32412kb
# 88ms
## 키 값에 입력 값이 들어가고 밸류에 그 값보다 작은 수의 갯수

n = int(input())
l = {0:0}
for i in map(int, input().split()):
    for j in list(l.keys()):
        if l[j] < i :
            if j+1 not in l or l[j+1] > i :
                l[j+1] = i
print(max(l))
# 32412kb
# 44ms
## 키 값에 부분 수열의 길이가 들어가고 밸류에 같은 길이의 부분 수열의 끝 값 중 가장 작은 값

n = int(input())
l = {0:0}
for i in map(int, input().split()):
    for j in range(len(l)-1,-1,-1):
        if l[j] < i :
            if j+1 not in l or l[j+1] > i :
                l[j+1] = i
                break
print(len(l)-1)
# 32412kb
# 40ms