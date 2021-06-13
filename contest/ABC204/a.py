x, y = map(int,input().split())
ans ='012'
if x == y:
  ans = x
else:
  ans = ans.replace(str(x),'').replace(str(y),'')
print(ans)