n = int(input())
a = list(map(int,input().split()))
a.sort(reverse=True)
b = list(map(str,a[:3]))

ans = 0
ans = max(int(b[0]+b[1]+b[2]),ans)
ans = max(int(b[0]+b[2]+b[1]),ans)
ans = max(int(b[1]+b[0]+b[2]),ans)
ans = max(int(b[1]+b[2]+b[0]),ans)
ans = max(int(b[2]+b[0]+b[1]),ans)
ans = max(int(b[2]+b[1]+b[0]),ans)
print(ans)
