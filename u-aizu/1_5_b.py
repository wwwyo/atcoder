h, w = map(int, input().split())

while not(h == 0 and w == 0):
  limit = '#' * w + '\n'
  inner = '#' + ('.' * (w-2)) + '#\n'
  inner *= (h-2)
  print(limit + inner +limit)
  h, w = map(int, input().split())