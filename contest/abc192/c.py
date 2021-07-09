n,k = map(int,input().split())

for i in range(k):
  # if n == 0: break
  n = list(str(n))
  n = int(''.join(sorted(n,key=int,reverse=True))) - int(''.join(sorted(n,key=int)))
print(n)
