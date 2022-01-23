
from itertools import permutations
import sys
sys.setrecursionlimit(10**8)
# 8
n = int(input())
a = []
for _ in range(2*n-1):
    a.append(list(map(int,input().split())))

# for i in range(2*n-2):
#     cnt = 0
#     for j in range(i+1,2*n-1):
#         cnt += a[i][j-i-1]
#     ans = max(ans,cnt)
# print(ans)
ans = []
all_lst = set()
def recursive(ini,cnt,lst):
    if len(lst) == 2*n:
        # print(cnt,lst)
        ans.append(cnt)
        return
    for i in range(ini,n):
        if lst & {i}:
            continue
        for j in range(i+1,2*n):
            if lst &{j}:
                continue
            # print(i,j,a[i][j-i-1])
            recursive(i+1,cnt ^ a[i][j-i-1],lst | {i,j})
    # if len(lst) == 2*n:
    #     ans.append(cnt)
    #     return
    # for i in range(2*n-1):
    #     if lst & {i}:
    #         continue
    #     if prev != -1:
    #         if prev < i:
    #             i,prev = prev,i
    #         recursive(-1,cnt ^ a[i][prev-i-1],lst | {i})
    #     else:
    #         recursive(i,cnt,lst | {i})


recursive(0,0,set())
print(max(ans))







# 1,2,3,4,5,6
# 1,2
# 1,3
# 1,4

