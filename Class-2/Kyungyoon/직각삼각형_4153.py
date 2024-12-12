num_list = []

while True:
    line = list(map(int, input().split()))
    if line == [0, 0, 0]:
        break
    num_list.append(line)
    
for line in num_list:
    a = line[0]
    b = line[1]
    c = line[2]
    if (a**2 == b**2 + c**2) or (b**2 == a**2 + c**2) or (c**2 == a**2 + b**2):
        print('right')
    else:
        print('wrong')