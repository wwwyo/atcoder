
import sys
from itertools import accumulate
# 500,10**5,10**5
n,m,Q = map(int,input().split())
rails = [[0] * n for _ in range(n)]

for line in range(m):
    l,r = map(int,input().split())
    rails[l-1][r-1] += 1

rails = [list(accumulate(s)) for s in rails]
# for s in zip(*rails):
    # print(list(accumulate(reversed(s))))
rails = [list(reversed(list(accumulate(reversed(s))))) for s in zip(*rails)]

# print(rails)
for line in range(Q):
    p,q = map(int,input().split())
    print(rails[q-1][p-1])