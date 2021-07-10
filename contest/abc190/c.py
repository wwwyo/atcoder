n,m = map(int,input().split())
ab = [list(map(int,input().split())) for _ in range(m)]
k = int(input())
cd = [list(map(int,input().split())) for _ in range(k)]
import itertools

dish = [0]*100
combs = list(itertools.product(*cd))
m = 0
for comb in combs:
  cnt = 0
  for j in ab:
    if j[0] in comb and j[1] in comb:
      cnt+=1
  m = max(m,cnt)
print(m)