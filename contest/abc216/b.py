n = int(input())
name = [list(input().split()) for _ in range(n)]
for i in range(len(name)-1):
    for j in range(i+1, len(name)):
        if (name[i][0] == name[j][0] and name[i][1] == name[j][1]):
            print('Yes')
            exit()
print('No')
