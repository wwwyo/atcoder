from collections import deque

if __name__ == '__main__':
    # max(m) = 36
    # >>> math.factorial(9)
    # 362880通り
    n = 9
    m = int(input())

    # 頂点数9
    edge = [[] for _ in range(n)]
    for _ in range(m):
        u,v = map(lambda x: int(x)-1,input().split())
        edge[u].append(v)
        edge[v].append(u)

    # コマjの初期値頂点

    p = list(map(lambda x:int(x)-1,input().split()))
    goal = list(range(0,9))
    goal[8] = -1
    # s[頂点] = コマ
    s = [-1] * 9
    for i,v in enumerate(p):
        s[v] = i

    q = deque([(s,0)])

    visited = {tuple(s):0}
    while len(q):
        s,cnt = q.popleft()
        cnt+=1
        emp_idx = s.index(-1)
        for node in edge[emp_idx]:
            state = s[:]
            state[node],state[emp_idx] = -1,state[node]
            if visited.get(tuple(state)) == None:
                visited[tuple(state)] = cnt
                q.append((state,cnt))

    if visited.get(tuple(goal)) != None:
        print(visited[tuple(goal)])
    else:
        print(-1)

