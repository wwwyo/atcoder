n = int(input())
arr = sorted(list(map(int, input().split())), reverse=True)
a = 0
b = 0
for i in arr:
  if a <= b:
    a += i
  else:
    b += i

print(max([a, b]))
