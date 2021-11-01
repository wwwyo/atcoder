# A
# 行：10**100
# 列：7
# B N x M
# (i-1) * 7 + j
# (x-j)/7 + 1

import math
n,m = map(int,input().split())

b = []
for _ in range(n):
    tmp = list(map(int,input().split()))
    b.append(tmp)

start = b[0][0]
for j in range(1,8):
# a_i = math.ceil((start - 1) //7)+1
# a_j = (start-1) % 7+1
# print(a_i,a_j)
    if (start - j+7) % 7 == 0:
        a_i = (start-j +7) // 7
        a_j = j
        break

# if a_j + m > 7:
#     print('No')
#     exit()
# ! すり抜けるやつがある
for i in range(n):
    for j in range(m):
        # if (i + a_i) != (b[i][j] - (j+a_j) + 7) // 7:
        a = (a_i + i -1) * 7 + (a_j + j)
            # print(a)
            # print(b[i][j])
        if b[i][j] != a:
            print('No')
            exit()
# wa 5
# これでwa3まで減る
if a_j+m > 7:
    print('No')
    exit()
# b[0][j]チェック
# # カレンダーの終端が最終行以外であった時
for j in range(m):
    if b[0][j] % 7 == 0 and j != m -1:
        print('No')
        exit()
# for i in range(n):
#     for j in range(m-1):
#         if b[i][j] +1 != b[i][j+1]:
#             print('No')
#             exit()
# for i in range(n-1):
#     for j in range(m):
#         if b[i][j] +7 != b[i+1][j]:
#             print('No')
#             exit()



print('Yes')


