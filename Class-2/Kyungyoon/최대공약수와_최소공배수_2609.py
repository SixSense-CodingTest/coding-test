"""
최대공약수
유클리드 호제법의 원리: 두 수 A, B의 최대공약수는 B와 A % B의 최대공약수와 같다.
반복문을 통해 나머지가 0이 될 때까지 N과 M의 값을 교환하며 나머지를 구한다.

최소공배수
a와 b의 곱을 최대공약수로 나눈 값이 최소공배수
"""
N, M = map(int, input().split())
a, b = N, M

while M != 0:  # 나머지가 0이 될 때까지 반복
    N, M = M, N % M  # N에 M을 대입하고, M에 N % M의 값을 대입


bae = (a * b) // N  

print(N)  
print(bae) 

"""
PyPy3
메모리 : 108384KB
시간 : 92ms

Python3
메모리 : 32412KB
시간 : 40ms
"""