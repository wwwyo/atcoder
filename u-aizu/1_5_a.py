h, w = map(int, input().split())
while h != 0 and w != 0:
  ans = '#'
  ans *= w
  ans += '\n'
  ans *= h
  print(ans)
  h, w = map(int, input().split())