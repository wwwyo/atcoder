# 今回の問題は木の直径を求めることができれば良い。=>端同士を結べば良いから
# 単純に考えると全てのノードからbfsで最大距離を求めることができるがO(n**2)でtleする
# ただO(n)で探索可能なアルゴリズムがある。


#! 木の直径は最短距離計算を2回やる
# 1回目で端をみつける
# ２回目で直径がもとまる
# 証明：https://qiita.com/nomikura/items/a4c5be6c72ce854d7ce4

#!この条件が必須=> どの都市の間も、いくつかの道路を通って移動可能

from collections import deque

# bfs
def bfs(tree, ini):
    queue = deque()
    visited = set()

    # 終端ノード
    last_node = 0
    # 距離
    step = 0

    queue.append(ini)
    visited.add(ini)
    while len(queue) > 0:
        new_queue = deque()
        for node in queue:
            for next in tree[node]:
                if not next in visited:
                    visited.add(next)
                    new_queue.append(next)
                    last_node = next
        step +=1
        queue = new_queue

    return step,node

if __name__ == '__main__':
    n = int(input())
    tree = [[] for _ in range(n)]
    for _ in range(n-1):
        v,u = map(lambda x: int(x) -1,input().split())
        tree[v].append(u)
        tree[u].append(v)

    # 都市1から出発した時の最適パターンを見つける
    step, node = bfs(tree,0)
    step,node = bfs(tree,node)
    print(step)
