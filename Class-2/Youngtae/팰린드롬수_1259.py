# 팰린드롬수 = 앞뒤가 똑같은 단어

while True:
    number = input()
    if number == '0':
        break
    if number[::-1] == number:
        print('yes')
    else:
        print('no')



