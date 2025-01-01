def isFizzBuzz(n):
    if n % 3 == 0 and n % 5 == 0:
        return 'FizzBuzz'
    elif n % 3 == 0 and n % 5 != 0:
        return "Fizz"
    elif n % 3 != 0 and n % 5 == 0:
        return "Buzz"
    else:
        return n


s_list = [input() for i in range(3)]
num_index = None
num = None

for idx, i in enumerate(s_list):
    if i.isnumeric():
        num_index = idx
        num = int(i)
        break

print(isFizzBuzz(num+3-int(num_index)))
