a, b, c = map(int, input().split())
ans = []
for i in range(1, c+1):
  if c % i == 0 and (a <= i and b >= i):
    ans.append(i)
print(len(ans))