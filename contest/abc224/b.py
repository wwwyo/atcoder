# max(50)
h,w = map(int,input().split())
a = []
for i in range(h):
    a.append(list(map(int,input().split())))

for i in range(h-1):
    for j in range(w-1):
        if a[i][j] + a[i+1][j+1] > a[i+1][j] + a[i][j+1]:
            print('No')
            exit()

print('Yes')
