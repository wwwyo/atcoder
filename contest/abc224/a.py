# import numpy as np

# max(300)
n = int(input())
ans = n * (n-1) * (n-2) / (6)
# 直線上にあるかチェック
lst = []
for _ in range(n):
    lst.append(list(map(int,input().split())))

for i in range(n-2):
    for j in range(i+1, n-1):
        for k in range(j+1, n):
            x1,y1 = lst[i]
            x2,y2 = lst[j]
            x3,y3 = lst[k]
            dx1 = x1 - x2
            dy1 = y1 - y2
            dx2 = x3 - x2
            dy2 = y3 - y2
            if (dx1 * dy2 == dx2 * dy1):
                ans-=1
            # a_b = (x1-x2) ** 2 + (y1-y2) ** 2
            # b_c = (x2-x3) ** 2 + (y2-y3) ** 2
            # a_c = (x1-x3) ** 2 + (y1-y3) ** 2
            # if a_b + a_c == b_c or a_b + b_c == a_c or a_c + b_c == a_b:
            #     ans-=1

print(int(ans))

