n = int(input())
xy = [list(map(int,input().split())) for _ in range(n)]
y = []
for i in range(len(xy)-1):
    for j in range(i+1, len(xy)):
        if xy[i][0] == xy[j][0]:
            y.append((xy[i][1],xy[j][1]))


ans = 0
for i in range(len(y)-1):
    for j in range(i+1, len(y)):
        if y[i] == y[j] or y[i] == (y[j][1],y[j][0]):
            ans += 1
print(ans)
