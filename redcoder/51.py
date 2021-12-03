import math
import bisect
# 10^5
# n = int(input())
# a = [int(input()) for _ in range(n)]

# lis = [a[0]]

# for i in range(n):
#     if a[i] > lis[-1]:
#         lis.append(a[i])
#     else:
#         idx = bisect.bisect_left(lis, a[i])
#         lis[idx] = a[i]

# print(len(lis))
n = int(input())
a = [int(input()) for _ in range(n)]
dp = [math.inf] * n
dp[0] = a[0]
len_ = 0

def binSearch(n,low,high):
    while low <= high:
        mid = (low+high)//2
        if dp[mid] > n:
            high = mid-1
        elif dp[mid] < n:
            low = mid+1
        else:
            return mid
    if dp[mid] < n:
        return mid+1
    elif dp[mid] >= n:
        return mid

for i in range(1,n):
    if dp[len_] < a[i]:
        len_+=1
        dp[len_] = a[i]
    else:
        idx = bisect.bisect_left(dp,a[i])
        dp[idx] = a[i]
print(len_+1)