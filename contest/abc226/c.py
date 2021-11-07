# n = 2 * 10^5
# t = 10^9
from collections import deque
n = int(input())
time_lst = []
r_len = []
requires = []
for _ in range(n):
    tka = list(map(int,input().split()))
    time_lst.append(tka[0])
    r_len.append(tka[1])
    requires.append(tka[2:])

t = time_lst[-1]
req_l = [-1]
req = requires[-1]

learning = deque(req)
total = t
having = {}

while learning:
    skill = learning.popleft()
    if having.get(skill):
        continue
    else:
        having[skill] = True
        total += time_lst[skill-1]
        for r in requires[skill-1]:
            if not having.get(r):
                learning.append(r)





print(total)