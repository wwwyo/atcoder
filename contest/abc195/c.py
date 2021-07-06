n = int(input())
l = len(str(n))
ans=0

if l >= 4:
  ans+=n-999
if l >= 7:
  ans+=n-999999
if l >= 10:
  ans+=n-999999999
if l >= 13:
  ans+=n-999999999999
if l >= 16:
  ans+=1
print(ans)
