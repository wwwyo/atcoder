# 有効グラフの互いに行き来が可能な頂点の集合＝＞強連結成分(SCC)を使う

# https://hkawabata.github.io/technical-note/note/Algorithm/graph/scc.html
# https://zenn.dev/m193h/articles/c9495557d135a4
# dfsの帰りがけに頂点番号をラベリング
# 有効グラフが片方から伸びているものを見つける（上流・下流）
# G'ができる

from sys import setrecursionlimit
setrecursionlimit(10**7)


def comb(n,k):
    return

def dfs(now: int, seen: list, edge: list,post_order):
    if seen[now]:
        return
    seen[now] = 1
    for node in edge[now]:
        if seen[node]: continue
        dfs(node)

    post_order.append(now)
    return

def re_dfs(now: int, seen: list, edge: list):
    
    return


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
    post_order = []
    for i in range(n):
        dfs(i,seen,edge,post_order)

    ans = 0
    seen = [0] * n

