N, r, c = map(int, input().split())
print(int('0'.join(list(f'{r:b}'))+'0',2)+int('0'.join(list(f'{c:b}')),2))
# 32412kb
# 36ms

# r에 대한 규칙
# 0 2 8 10 32 34 40 42 128 130 136
'''
00000000 0
00000010 1
00001000 2
00001010 3
00100000 4
00100010 5
00101000 6
00101010 7
10000000 8
10000010 9
10001000 10
10001010 11
10100000 12
10100010 13
10101000 14
10101010 15
'''
# r을 2진법으로 변환 후 사이에 0을 넣고 맨 뒤에도 0 넣은 뒤 10진법으로 변환
# c와 동일한 연산 후 2배

# c에 대한 규칙
# 0 1 4 5 16 17 20 21 64 65 68 69 80 
'''
0000000 0 4진법 000000
0000001 1 4진법 000001
0000100 2 4진법 000010
0000101 3 4진법 000011
0010000 4 4진법 000100
0010001 5
0010100 6
0010101 7
1000000 8
1000001 9
1000100 10
1000101 11
1010000 12
1010001 13
1010100 14
1010101 15
'''
# c를 2진법으로 변환 후 사이에 0을 넣고 다시 10진법으로 돌림

N, r, c = map(int, input().split())
print(2*int((f'{r:b}'),4)+int(f'{c:b}',4))
# 2진법 변환후 바로 4진법인 것 취급하여 다시 10진법으로 돌려도 됨
# 32412kb
# 44ms 속도는 좀 더 느림