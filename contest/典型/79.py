# 100
h,w = map(int,input().split())
# 自分、右、下、右下を変えることができる
a = []
b = []
for _ in range(h):
    a.append(list(map(int,input().split())))

for _ in range(h):
    b.append(list(map(int,input().split())))

d = [(0,0),(0,1),(1,0),(1,1)]
cnt = 0
for i in range(h):
    for j in range(w):
        if i == (h-1) or j == (w-1):
            if a[i][j] != b[i][j]:
                print('No')
                exit()
        a_ = a[i][j]
        b_ = b[i][j]
        diff = a_-b_
        if diff == 0:
            continue
        else:
            cnt+=abs(diff)
            for dx,dy in d:
                a[i+dx][j+dy]-=diff
print('Yes')
print(cnt)
