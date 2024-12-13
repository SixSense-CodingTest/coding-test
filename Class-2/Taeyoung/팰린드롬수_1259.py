import sys

while True:
    pd = sys.stdin.readline().strip()
    if pd == '0': break

    pd_len = len(pd)

    if pd == pd[::-1]:
        print("yes")
    else:
        print("no")
