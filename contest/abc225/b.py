# max(n) = 10 ** 5
n = int(input())
edge = [0] * (n+1)
for _ in range(n-1):
    a,b = map(int,input().split())
    edge[a] += 1
    edge[b] += 1
if sorted(edge)[-1] == n-1:
    print('Yes')
else:
    print('No')

