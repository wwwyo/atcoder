n = int(input())
t = [list(map(int,input().split())) for _ in range(n)]
now = [0,0]
time = 0

for i in t:
  past = i[0] - time
  stop = abs(i[1] - now[0]) + abs(i[2] - now[1])
  if stop > past:
    break
  elif (past - stop) %2 != 0:
    break

  now = [i[1],i[2]]
  time = i[0]
else:
  print('Yes')
  exit()

print('No')

