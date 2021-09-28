n,l = map(int,input().split())
k = int(input())
a = list(map(int,input().split()))
a.append(l)

# 最小値の最大かは二分探索
# O(NlogL)
# 区間一つあたりの長さをメモしていく
# leftは分割可能
# right以上は分割不可能

def isDivide(mid: int):
    tmp = 0
    cnt = 0
    for i in a:
        if i - tmp >= mid:
            tmp = i
            cnt +=1
    if cnt > k:
        return True
    return False

left = 0
right = l
while right - left > 1:
    mid = (left + right)//2
    if isDivide(mid):
        left = mid
    else:
        right = mid

print(left)