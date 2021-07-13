n,x = map(int,input().split())
a = sum(list(map(int,input().split())))

if (a - n//2) <= x:
  print('Yes')
else:
  print('No')

