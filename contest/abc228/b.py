# 10^5
n,x = map(int,input().split())
a = list(map(int,input().split()))

x-=1
done = False
cnt = 1
notice = [0] * n
notice[x] = 1
while not done:
    new_notify = a[x]-1
    if not notice[new_notify]:
        notice[new_notify] = 1
        x = new_notify
        cnt+=1
    else:
        done = True
print(cnt)