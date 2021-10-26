
# ! あきらめ
# max(n) = 10**5
n = int(input())

# n^2の距離の和
edge = [[] for _ in range(n)]
for _ in range(n-1):
    a,b = map(lambda x: int(x)-1,input().split())
    edge[a].appned(b)
    edge[b].appned(a)

# aのbfs
