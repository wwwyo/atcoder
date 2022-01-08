import math
# 100
n = int(input())
coo = []
max_ = 0
for _ in range(n):
    coo.append(list(map(int,input().split())))
for i in range(n-1):
    for j in range(i+1,n):
        x_1,y_1 = coo[i]
        x_2,y_2 = coo[j]
        # print(x_1,y_1,x_2)
        max_ = max(max_,math.sqrt((x_1 - x_2) ** 2 + (y_1 - y_2) ** 2 ))
print(max_)

