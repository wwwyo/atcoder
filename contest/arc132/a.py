# 10^5
n = int(input())
# 黒のますの数行列 rxc
r = list(map(int,input().split()))
c = list(map(int,input().split()))
q = int(input())
# dist = [[-1] * n for _ in range(n)]

ans = []
for _ in range(q):
    r_i,c_i = map(int,input().split())
    if r[r_i-1]+c[c_i-1] >n:
        ans.append('#')
    else:
        ans.append('.')
print(*ans,sep="")
