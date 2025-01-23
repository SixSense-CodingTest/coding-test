def solve(n):
    for _ in range(n):
        node, edge, hole = map(int, input().split())
        edges = [[] for _ in range(node+1)]
        graph = [[0]*(node+1) for _ in range(node+1)]
        wh_st = set()
        for _ in range(edge):
            s, e, t = map(int, input().split())
            edges[s].append((e,t))
            edges[e].append((s,t))
        for _ in range(hole):
            s, e, t = map(int, input().split())
            edges[s].append((e,-t))
            graph[s][e] = -t
            wh_st.add((s,e))

        while wh_st:
            st, mid = wh_st.pop()
            for ed, time in edges[mid]:
                if graph[st][mid] + time < graph[st][ed]:
                    graph[st][ed] = graph[st][mid] + time
                    wh_st.add((st, ed))
                    if st == ed:
                        print('YES')
                        break
            else: continue
            break
        else: print('NO')
solve(int(input()))
# 36336kb
# 152ms