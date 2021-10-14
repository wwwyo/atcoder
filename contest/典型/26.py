# 探索済ノードの管理に気をつける！
# ノードを単純にリストに入れると時間超過するので
# フラグを立てて管理する

# 木は二部グラフになる
# 2 <= n <= 10**5

from sys import setrecursionlimit
setrecursionlimit(10**7)


#! 再帰だとタイムオーバーする
def dfs(now, color):
    # colors[color].append(now)
    # for node in edge[now]:
    #     if seen[node]:
    #         continue
    #     seen[node] = 1
    #     dfs(node, 1-color)
    # return
    done = True
    q = []
    q.append(now)
    while q:
        new_q = []
        for now in q:
            colors[color].append(now)
            for node in edge[now]:
                if seen[node]:
                    continue
                seen[node] = 1
                new_q.append(node)
        q = new_q
        color = 1 - color


if __name__ == '__main__':
    n = int(input())

    edge = [[] for _ in range(n+1)]
    for _ in range(n-1):
        a, b = map(int, input().split())
        edge[a].append(b)
        edge[b].append(a)

    start = 1
    seen = [0] * (n+1)
    seen[start] = 1
    colors = [[], []]
    dfs(start, 0)
    if len(colors[0]) >= n//2:
        print(*colors[0][:n//2])
    else:
        print(*colors[1][:n//2])
