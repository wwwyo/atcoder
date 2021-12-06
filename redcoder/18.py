# 10^5
n = int(input())
s = sorted(list(map(int,input().split())))
q = int(input())
t = list(map(int,input().split()))

def bin_search(i):
    high = n-1
    low = 0
    while low <= high:
        mid = (low+high)//2
        if i < s[mid]:
            high = mid-1
        elif i > s[mid]:
            low = mid+1
        else:
            return True
    return False


ans = 0
for i in range(q):
    if bin_search(t[i]):
        ans+=1
print(ans)

