import collections

n = int(input())
a = dict(collections.Counter(map(int,input().split())))
b = list(map(int,input().split()))
c = list(map(int,input().split()))
cnt = 0

for i in c:
    try:
        cnt += a[b[i-1]]
    except:
        continue
print(cnt)

