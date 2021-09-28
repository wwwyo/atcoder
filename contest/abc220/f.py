# 木のすべての頂点について, その頂点を根としたときの木DPを高速に行う.
from collections import deque

n = int(input())
tree = [[] for _ in range(n)]
for _ in range(n-1):
    u,v = map(int,input().split())
    u -=1
    v -=1
    tree[u].append(v)
    tree[v].append(u)


# 探索済みパスメモ
visited = set()
visited.add(0)
# 探索パス
queue = deque()
queue.append(0)
# 各ノードへの到達ステップ数
step = [None] * n
step[0] = 0
while len(queue) > 0:
    q = queue.popleft()
    for v in tree[q]:
        if not v in visited:
            visited.add(v)
            queue.append(v)
            step[v] = step[q] + 1


# https://zenn.dev/m193h/articles/20210926sun230842m193habc220
def search_num_child(now: int):
    # 0を根とした木において、頂点now以下の頂点数(頂点nowとその子の数)をdfsで求める
    if num_child[now]:
        return num_child[now]
    num_child[now] = 1
    for n_node in tree[now]:
        if num_child[n_node]:
            continue
        num_child[now] += search_num_child(n_node)
    return num_child[now]

n = int(input())
tree = [[] for _ in range(n)]
for _ in range(n-1):
    u,v = map(int,input().split())
    u -=1
    v -=1
    tree[u].append(v)
    tree[v].append(u)
# num_child[i] = 頂点０を根としたiの部分技の大きさ（iを含む）
num_child = [0] * n
search_num_child(0)
dis_from_zero = sum(num_child) -n

# oを根としてbfsで高さが低い頂点から(oに近い頂点から)ansを求めていく
ans = [dis_from_zero]
seen = [0] * N
queue = deque([(0,0)])
while queue:
    now, parents = queue.popleft()
    seen[now] = 1

    if now:
        res = ans[parents]
        res -= num_child[now]
        

print(tree)
print(sum(step))