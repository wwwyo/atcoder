# 300
import math


def warshallFloyd():
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])


if __name__ == "__main__":
    n,m = map(int,input().split())
    dist = [[math.inf] * n for _ in range(n)]

    for _ in range(m):
        a,b,t = map(int,input().split())
        dist[a-1][b-1] = t
        dist[b-1][a-1] = t
    for i in range(n):
        dist[i][i] = 0
    warshallFloyd()
    # 引っ越したあと、最も長くバスに乗らないといけないときにかかる時間
    max_ = []
    for i in range(n):
        max_.append(max(dist[i]))
    print(min(max_))

