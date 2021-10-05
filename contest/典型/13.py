# https://www.youtube.com/watch?v=X1AsMlJdiok
# 最短経路はダイクストラ
# 頂点s から任意の頂点に行く最短経路を一気に計算できる。
# O((N+M)log(N))

# 始点に0を書き込む
# 未確定の地点から最小なものを確定する
# 確定した地点から1ステップでいける地点の重みを更新する
# 全ての地点の重みが確定するまで繰り返す

from heapq import heappush, heappop


def dijkstra(start, edge):
    # def dijkstra(s, graph):  # (始点, グラフのリスト)
    #     INF = 10 ** 18
    #     dist = [INF] * n  # INF で初期化
    #     check = [False] * n  # Bool
    #     dist[s] = 0
    #     q = [(0, s)]  # （距離・ノード）
    #     while q:
    #         v = heappop(q)[1]  # 今いるノード
    #         if check[v]:
    #             continue  # すでに行っていたらcontinue
    #         check[v] = True  # 訪問済み
    #         for i, j in graph[v]:  # 先のノード・距離
    #             if check[i] != False:
    #                 continue
    #             if dist[i] <= dist[v] + j:
    #                 continue
    #             dist[i] = dist[v] + j
    #             heappush(q, (dist[i], i))  # 必ず[0]が距離になるように（優先度付きキュー）
    #     return dist
    INF = 10 ** 18
    # 移動コスト, 始点
    q = [(0, start)]
    costs = [INF] * n
    costs[start] = 0
    check = [False] * n

    while q:
        min_cost, min_node = heappop(q)
        if check[min_node]:
            continue
        check[min_node] = True
        # min_node = min(q, key=q.get)
        # node_ans[min_node] = q[min_node]

        next = edge[min_node]
        for node, value in next:
            costs[node] = min(min_cost + value, costs[node])
            heappush(q, (costs[node], node))
    return costs


if __name__ == '__main__':
    # n,m 10^5
    n, m = map(int, input().split())
    edge = [[] for _ in range(n)]
    for _ in range(m):
        a, b, c = map(int, input().split())
        a -= 1
        b -= 1
        edge[a].append((b, c))
        edge[b].append((a, c))

    from_start_to_k = dijkstra(0, edge)
    from_end_to_k = dijkstra(n-1, edge)
    # output: 1 => k => n
    for k in range(n):
        print(from_start_to_k[k] + from_end_to_k[k])
