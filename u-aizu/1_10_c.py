import math
n = int(input())
s = list(map(int, input().split()))
while True:
    av = float(sum(s)/n)
    ans = float(0)
    for i in s:
        ans += (i - av)**2
    print(float(math.sqrt(ans/n)))
    n = int(input())
    if n == 0:
        break
    s = list(map(int, input().split()))
