import collections
n = int(input())
a = map(lambda x: int(x)%200,input().split())
cnt=0

for k,v in collections.Counter(a).items():
  cnt+=int(v*(v-1)/2)
print(cnt)