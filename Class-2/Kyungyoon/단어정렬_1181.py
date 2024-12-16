"""
* 배운 내용 *

sort
- 반환값이 없음 = 변수에 저장 하면 안됨 = print 문 안에 바로 넣을 수 없음
- 위에처럼 str_list.sort()하고 print해야함

sorted
- 반환값이 있음 = 변수에 저장해줘야함 = print문 안에 바로 넣을 수 있음
"""

N = int(input())
str_list = []
for _ in range(N):
    str = input()
    str_list.append(str)

str_list = list(set(str_list))
str_list.sort(key= lambda x: (len(x),x))
print(*str_list, sep='\n')

"""
PyPy3
메모리 : 116376KB
시간 : 172ms

Python3
메모리 : 37024KB
시간 : 568ms
"""