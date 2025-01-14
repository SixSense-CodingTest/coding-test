N = int(input())

p_graph = {}
c_graph = {}


for i in range(N):
    t1,t2,t3 = input().split()
    p_graph[t1] = [t2,t3]

def left(node):

    print(node, end = '')
    if p_graph[node][0]!='.':
        left(p_graph[node][0])
    if p_graph[node][1]!='.':
        left(p_graph[node][1])

def middle(node):
    if p_graph[node][0]!='.':
        middle(p_graph[node][0])
    print(node, end = '')
    if p_graph[node][1]!='.':
        middle(p_graph[node][1])
    

def right(node):
    if p_graph[node][0]!='.':
        right(p_graph[node][0])
    if p_graph[node][1]!='.':
        right(p_graph[node][1])
    print(node, end = '')

left('A')
print()
middle('A')
print()
right('A')

