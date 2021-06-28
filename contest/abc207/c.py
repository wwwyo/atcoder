n = int(input())
tlr = [list(map(int,input().split())) for _ in range(n)]
cnt = 0
for i in range(len(tlr)-1):
    t,l,r = tlr[i]
    for j in range(i+1, len(tlr)):
        tj,lj,rj = tlr[j]
        if r < lj or l > rj:
            continue
        elif r == lj:
            if not(t in [1,3] and tj in [1,2]):
                continue
        elif l == rj:
            if not(t in [1,2] and tj in [1,3]):
                continue
        cnt+=1

print(cnt)