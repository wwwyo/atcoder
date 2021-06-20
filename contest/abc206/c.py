import collections
n= int(input())
a = list(map(int,input().split()))

cnt = int((n**2-n)/2)
for i in collections.Counter(a).values():
    if i == 1:
        continue
    cnt-=int((i**2-i)/2)
print(cnt)

