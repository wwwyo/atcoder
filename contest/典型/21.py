# 有効グラフの互いに行き来が可能な頂点の集合＝＞強連結成分(SCC)を使う

# https://hkawabata.github.io/technical-note/note/Algorithm/graph/scc.html
# https://zenn.dev/m193h/articles/c9495557d135a4
# dfsの帰りがけに頂点番号をラベリング
# 有効グラフが片方から伸びているものを見つける（上流・下流）
# G'ができる

from sys import setrecursionlimit
from math import factorial
setrecursionlimit(10**7)


def comb(n,k):
    return factorial(n) // (factorial(n-k) * factorial(k))

def dfs(now: int):
    if seen[now]:
        return
    seen[now] = 1
    for node in edge[now]:
        if seen[node]: continue
        dfs(node)

    post_order.append(now)
    return

def re_dfs(now: int):
    if seen[now]: return 0
    seen[now] = 1
    cnt = 1
    for node in re_edge[now]:
        if seen[node]: continue
        cnt += re_dfs(node)

    return cnt


if __name__ == '__main__':
    # m = 2 * 10 ^ 5
    n,m = map(int,input().split())

    edge = [[] for _ in range(n)]
    re_edge = [[] for _ in range(n)]

    for _ in range(m):
        a,b = map(lambda x: int(x)-1,input().split())
        edge[a].append(b)
        re_edge[b].append(a)

    # すべての頂点を帰りがけ順でメモ

    seen = [0] * n # 探索済チェック
    # 帰りがけ順をメモ
    post_order = []
    for i in range(n):
        dfs(i)

    ans = 0
    seen = [0] * n
    # 最大のラベルから逆グラフでdfs => 強連結成分が得られる
    for i in post_order[::-1]:
        cnt = re_dfs(i)
        if cnt < 2: continue

        # 強い連結成分の数コンビネーション2
        ans += comb(cnt,2)

    print(ans)
