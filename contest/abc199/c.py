n = int(input())
s = list(input())
q = int(input())
tab = [list(map(lambda x: int(x)-1,input().split())) for _ in range(q)]
flag = False
for t in tab:
  if t[0] == 0:
    if flag:
      if t[1] >= n:
        t[1] = t[1]-n
        t[2] = t[2]-n
      elif t[2] < n:
        t[1] = n+t[1]
        t[2] = n+t[2]
      else:
        t[1] = n+t[1]
        t[2] = t[2]-n
    s[t[1]],s[t[2]] = s[t[2]],s[t[1]]
  elif t[0] == 1:
    flag = not(flag)
if flag:
  s = s[n:] + s[:n]
print(''.join(s))