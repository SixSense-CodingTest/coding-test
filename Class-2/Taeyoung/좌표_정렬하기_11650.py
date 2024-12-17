import sys

N = int(sys.stdin.readline())

xy = [list(map(int, sys.stdin.readline().split())) for i in range(N)]

for x, y in sorted(xy, key=lambda x : (x[0], x[1])):
    print(x, y)

####################
# memory: 61144KB  #
# time:   352ms    #
####################