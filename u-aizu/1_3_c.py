for i in range(1, 3003):
  x, y = map(int, input().split())
  if x == y == 0:
    break
  if x > y:
    print("{} {}".format(y, x))
  else:
    print("{} {}".format(x, y))
