import math
p = int(input())
cnt=0

for i in reversed(range(1,11)):
  ii = math.factorial(i)
  cnt += int(p / ii)
  p = int(p % ii)
print(cnt)
