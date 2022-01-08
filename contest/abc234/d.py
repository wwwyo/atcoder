
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


n,k = map(int,input().split())
p = list(map(int,input().split()))

lst = sorted(p[:k])
q = deque(lst)
ini = q[0]
print(ini)
for i in range(k,n):
    if ini > p[i]:
        print(ini)
        continue
    else:
        q.popleft()
        q.append(p[i])
        q = deque(sorted(list(q)))
        ini = q[0]
        print(ini)
