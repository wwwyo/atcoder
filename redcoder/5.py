
# x,y 10^5
a,b,c,x,y = map(int,input().split())
ans = []
# if a <= c and b <= c:
#     ans = a * x + b * y
# elif a <= c and b > c:
#     if x > y:
#         ans = 2 * y * c + (x-y) * a
#     else:
#         ans = 2 * y * c
# elif a > c and b <= c:
#     if y > x:
#         ans = 2 * x * c + (y-x) * b
#     else:
#         ans = 2 * x * c
# else:
#     ans = 2 * max(x,y) * c
# print(ans)

ans.append(a * x + b * y)
ans.append(2 * c * max(x,y))
if x > y:
    ans.append(2 *c * y + (x-y) * a)
else:
    ans.append(2 * c * x + (y-x) * b)
print(min(ans))
