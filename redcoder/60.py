import math

def warshall_floyd():
    for k in range(v):
        for i in range(v):
            for j in range(v):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])


if __name__ == '__main__':
    # 頂点の数, 辺の数
    v,e = map(int,input().split())
    dist = [[math.inf] * v for _ in range(v)]
    for _ in range(e):
        s,t,d = map(int,input().split())
        dist[s][t] = d

    # 初期値をセット
    for i in range(v):
        dist[i][i] = 0
    warshall_floyd()
    # 負の経路
    for i in range(v):
        if dist[i][i]<0:

    # if sum(dist[i]) < 0:
            print('NEGATIVE CYCLE')
            exit()
    for i in range(v):
        print(*map(lambda x: 'INF' if x == math.inf else x, dist[i]))






