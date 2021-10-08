import math
t = int(input())
l,x,y = map(int,input().split())
r = l / 2
w = 2 * math.pi / t
# 10^4
q = int(input())

# 観覧車(0, -l/2 ~ l/2, 0 ~ l)
# 像の位置(x,y,0)
# 現在位置とxy平面に下ろした点と像の位置のタンジェントから計算する
for _ in range(q):
    e = int(input())
    theta = -w * e - math.pi / 2
    wheel_y = (r * math.cos(theta))
    wheel_z = l/2 + (r * math.sin(theta))


    height = wheel_z
    bottom = pow((wheel_y - y) ** 2 + x ** 2,0.5)
    ans = math.atan2(height,bottom)
    print(math.degrees(ans))
