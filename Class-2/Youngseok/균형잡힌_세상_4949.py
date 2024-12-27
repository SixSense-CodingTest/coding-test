import sys
input = sys.stdin.readline
print = sys.stdout.write
while (st:=input().rstrip()) != '.':
    st = ''.join(filter(lambda x: x in '[]().', st))
    while '[]' in st or '()' in st: st = st.replace('[]','').replace('()','')
    if st == '.': print('yes\n')
    else: print('no\n')
# 32412kb
# 64ms