# n = 2 * 10 ^5
n = int(input())
a = list(map(int, input().split()))
a.append(10**9+1)
# aを圧縮する
ans = [0] * n
init = 1
for i in range(n):
    if a[i] < a[i+1]:
        param = 1
    elif a[i] > a[i+1]:
        param = 0
    else:
        continue

    if param != init:
        ans[i] = 1
        init = param

print(*ans)


# aが大きい時に銀にして
# aが小さい時に金に変換
# 1が金を持っている時
# status = 1
# for i in range(n):
#     if status == 1:
#         if a[i] >= a[i+1]:
#             # 自分が最大化確かめる
#             print(1, end=" ")
#             status = 1 - status
#         else:
#             print(0, end=" ")
#     else:
#         if a[i] <= a[i+1]:
#             # 自分が最小か確かめる
#             print(1, end=" ")
#             print(1, end=" ")
#             status = 1 - status
#         else:
#             print(0, end=" ")
