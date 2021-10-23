from sys import setrecursionlimit
setrecursionlimit(10**8)

def is_correct(p):
    for i in range(9):
        if i != p[i]:
            return False
    return True

def recursive(prev_p,cnt,emp_node,prev_node):
    p = prev_p[:]
    print(p)
    if is_correct(p):
        print(cnt)
        exit()
    for node in edge[emp_node]:
        idx = edge[emp_node].index(node)
        del edge[emp_node][idx]

        if node == prev_node: continue
        p[emp_node] ,p[node] = p[node],p[emp_node]
        recursive(p,cnt+1,node,emp_node)


if __name__ == '__main__':
    # max(m) = 36
    m = int(input())

    # 頂点数9
    edge = [[] for _ in range(10)]
    for _ in range(m):
        u,v = map(int,input().split())
        edge[u].append(v)
        edge[v].append(u)

    # コマjの初期値頂点
    # 8
    p = list(map(int,input().split()))
    emp_node = (set(range(1,10)) - set(p)).pop()
    # [node] = コマ
    new_p = [0] * 10
    for i,v in enumerate(p):
        new_p[v] = i+1
    recursive(new_p,0,emp_node, emp_node)
    print(-1)






