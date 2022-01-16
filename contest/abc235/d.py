
# import math
# import heapq

# # 10**6
# a,n = map(int,input().split())

# """
# 1. x * a
# 2. x[-1] = x[0]
# *末尾が0じゃない or 2桁以上
# """

# ans = 1
# cnt = 0
# ans_cnt = math.inf
# answers = []
# heapq.heapify(answers)
# memo = {}
# lim = len(str(n))
# # >>>n
# while ans <= n:
#     if ans == n:
#         ans_cnt = cnt
#         break
#     ans *= a
#     cnt += 1
#     if ans >= 10:
#         heapq.heappush(answers, [cnt, ans])
#         memo[ans] = cnt

# def is_ok(ans_,cnt_):
#     return len(str(ans_)) <= lim and (not memo.get(ans_) or memo[ans_] > cnt_)

# while answers:
#     cnt,ans = heapq.heappop(answers)
#     # print(cnt,ans)
#     if ans == n:
#         print(min(ans_cnt, cnt))
#         exit()
#     # elif ans > n:
#     #     continue
#     if is_ok(ans *a,cnt+1):
#         heapq.heappush(answers, [cnt+1,ans*a])
#         # print('??',ans*a)
#         memo[ans*a] = cnt+1
#     # 逆転
#     ans_s = list(str(ans))
#     if ans_s[-1] == '0':
#         continue
#     ans_last = ans_s.pop()
#     ans = int(ans_last + ''.join(ans_s))
#     # print('--',ans)
#     if is_ok(ans,cnt+1):
#         heapq.heappush(answers, [cnt+1,ans])
#         memo[ans] = cnt+1

#     # if not memo.get(ans):
#     #     memo[ans] = 1
#     #     answers.append((ans, cnt+1))
#     #     answers.append((ans+a, cnt+2))

# if ans_cnt == math.inf:
#     print(-1)
# else:
#     print(ans_cnt)



# bfsすれば最初にでできたnodeが最小
from collections import deque
a,n = map(int,input().split())
lim = 10**len(str(n))
costs = [-1] * lim
q = deque()
q.append(1)
costs[1] = 0

while q:
    node = q.popleft()
    cost = costs[node]

    node_multi = node * a
    if node_multi < lim and costs[node_multi] == -1:
        costs[node_multi] = cost + 1
        q.append(node_multi)

    # 入れ替え
    node_str = list(str(node))
    node_last = node_str.pop()
    if node_last != "0" and len(node_str)>0:
        node_change = int(node_last + ''.join(node_str))
        if node_change < lim and costs[node_change] == -1:
            costs[node_change] = cost +1
            q.append(node_change)
print(costs[n])






