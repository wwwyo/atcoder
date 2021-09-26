n = int(input())
tree = [[None] for _ in range(n)]
for _ in range(n-1):
    u,v = map(int,input().split())
    tree[u].append(v)
    tree[v].append(u)


for i in range(n):
    ans = 0
    for j in range(n):
        if i == j:
            continue

        tree[i] 

    print(ans)