
# 10**6
m = int(input())
dist = []
search = []
for _ in range(m):
    dist.append(list(map(int,input().split())))
dist.sort()
n = int(input())
for _ in range(n):
    search.append(list(map(int,input().split())))
search.sort()

def selectDiff(i):
    if i >= (n-1):
        return [-1,-1]
    x_o,y_o = dist[0]
    x,y = search[i]
    return [x-x_o,y-y_o]

done = False
cnt = 0
while not done:
    diff_x,diff_y = selectDiff(cnt)
    if diff_x == diff_y == -1:
        break
    cnt += 1
    for i in range(m):
        for j in range(n):
            if [dist[i][0] + diff_x, dist[i][1] + diff_y] == search[j]:
                break
        else:
            break
    else:
        print(diff_x,diff_y)
        exit()
# print(-1)


