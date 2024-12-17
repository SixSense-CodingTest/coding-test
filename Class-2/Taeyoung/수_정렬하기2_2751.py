import sys

N = int(sys.stdin.readline())
print("\n".join(map(str, sorted(set(int(sys.stdin.readline()) for i in range(N))))))

####################
# memory: 135680KB #
# time:   844ms    #
####################
