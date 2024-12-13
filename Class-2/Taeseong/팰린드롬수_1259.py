while True:
    pal = input()

    if pal == '0':
        break 

    print('yes' if pal==pal[::-1] else 'no')