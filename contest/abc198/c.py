import math
r,x,y = map(int,input().split())
d = float(math.sqrt(x**2+y**2))
if d == r:
  print(1)
elif d <= 2*r:
  print(2)
else:
  print(math.ceil(d / r))