import math
n = int(input())
ans = {}

for i in range(2,int(math.sqrt(n))+1):
  for j in range(2,33):
    calc = i**j
    if calc > n:
      break
    ans[calc] = 1
print(n-len(ans))