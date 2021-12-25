# 100
n,m = map(int,input().split())
a = []
for _ in range(n):
    a.append(list(map(int,input().split())))

# 曲から2つ選ぶ10**4
# 全員を探索する10**6
ans = 0
for t_1 in range(m-1):
    for t_2 in range(t_1+1,m):
        tmp = 0
        for i in range(n):
            tmp += max(a[i][t_1],a[i][t_2])
        ans = max(ans,tmp)
print(ans)
        
    

