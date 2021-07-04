from operator import itemgetter
n,k = map(int,input().split())
a = list(map(int,input().split()))

a_idx = list(enumerate(a))
a_idx.sort(key=itemgetter(1))

ans = [k//n] * n
for i , a in a_idx[:int(k%n)]:
  ans[i] +=1 
print(*ans,sep="\n")