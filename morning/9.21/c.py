import numpy as np
n,x = map(int,input().split())

a = list(map(int,input().split()))
a.append(x)
a.sort()

# それぞれの座標の距離をとって最大公約数を求める
distance = set()
for i in range(n):
    distance.add(a[i+1]-a[i])

print(np.gcd.reduce(list(distance)))




