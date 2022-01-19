
from itertools import accumulate
from os import sep
# 125
h,w,k,v = map(int,input().split())
dist = []
dist_t = []
for _ in range(h):
    dist.append(list(accumulate([0]+list(map(int,input().split())))))

for lst in zip(*dist):
    dist_t.append(list(accumulate([0]+list(lst))))
# print(dist_t,sep="\n")

ans = 0
for i_l in range(1,w+1):
    for j_l in range(1,h+1):
        for i_r in range(i_l,w+1):
            for j_r in range(j_l, h+1):
                cnt = (i_r - i_l+1) * (j_r-j_l+1)
                money = dist_t[i_r][j_r] - dist_t[i_l-1][j_r] - dist_t[i_r][j_l-1] + dist_t[i_l-1][j_l-1]
                money+=(cnt*k)
                if money <= v:
                    ans = max(ans,cnt)
print(ans)



# 0 0 0 0 0
# 0 1 1 1 1
# 0 1 1 1 1
# 0 1 1 1 1
# 0 1 1 1 1

# 1 2 3 4
# 1 2 3 4
# 1 2 3 4
# 1 2 3 4

# 1 2 3 4
# 2 4 6 8
# 3 6 9 12
# 4 8 12 16

