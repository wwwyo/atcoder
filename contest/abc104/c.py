import math
d, g = map(int,input().split())
g = g//100
pc = [list(map(int,input().split())) for _ in range(d)]

ans = 10*100
for i in range(2**d):
    s=0
    ans_= 0
    for j in range(d):
        if i >> j &1:
            s+=pc[j][1]//100+ pc[j][0]*(j+1)
            ans_+= pc[j][0]
    if s >= g:
        ans = min(ans,ans_)
    else:
        for j in range(d-1,-1,-1):
            if not((i>>j)&1):
                if (s + pc[j][0]*(j+1))>=g:
                    h=math.ceil((g-s)/(j+1))
                    s+=(h*(j+1))
                    ans_+=h
                    ans = min(ans,ans_)
                    break
                else:
                    break
print(ans)