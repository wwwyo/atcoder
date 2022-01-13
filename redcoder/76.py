
# n:3000
# 累積和
n = int(input())
a = list(map(int,input().split()))

# def multipleSum(i):
#     head = 0
#     prev = sum(a[:i])
#     ans = prev
#     for j in range(i,n):
#         prev = prev - a[head] + a[j]
#         if a[head] < a[j]:
#             ans = max(ans,prev)
#         head += 1
#     return ans


# for i in range(1,n+1):
#     print(multipleSum(i))

# [i,k)
s = [0] * (n+1)

for i in range(n):
    s[i+1] = s[i] + a[i]

# 区間
for l in range(1,n+1):
    # 左端
    ans = 0
    for i in range(0,n-l+1):
        ans = max(ans, s[l+i] - s[i])
    print(ans)

    # 0,1,2,3,4,5
