import sys

N = int(sys.stdin.readline())

people = []

for i in range(N):
    age, name = map(str, sys.stdin.readline().split())
    people.append([int(age), name])

for i in sorted(people, key=lambda x: x[0]):
    print(f'{i[0]} {i[1]}')

####################
# memory: 48852KB  #
# time:   236ms    #
####################