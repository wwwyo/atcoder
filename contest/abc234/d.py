
from collections import deque
# import bisect
# # 10**5,
# n,k = map(int,input().split())
# p = list(map(int,input().split()))

# # 初期値
# lst = sorted(p[:k])
# print(lst[-k])

# for i in range(k,n):
#     bisect.insort_left(lst,p[i])
#     print(lst[-k])


# 優先度付きキューで管理すればいけた
import heapq
n,k = map(int,input().split())
p = list(map(int,input().split()))

q = p[:k]
heapq.heapify(q)
print(q[0])
for i in range(k,n):
    if q[0] < p[i]:
        heapq.heappop(q)
        heapq.heappush(q,p[i])
    print(q[0])



