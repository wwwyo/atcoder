alp = list('abcdefghijklmnopqrstuvwxyz')
p = list(map(int, input().split()))
for i in p:
    print(alp[i-1], end = '')
