# 10^5
from statistics import median
n = int(input())
#!違う 45度回転させて中心を求める
# x,yを独立に考える

x_dict = []
y_dict = []
for _ in range(n):
    x,y = map(int,input().split())
    x_dict.append(x)
    y_dict.append(y)

center_x = int(median(x_dict))
center_y = int(median(y_dict))


ans = 0

for i in range(n):
    ans += abs(center_x - x_dict[i]) + abs(center_y - y_dict[i])
print(ans)
