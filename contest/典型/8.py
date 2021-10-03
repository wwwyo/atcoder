# n = 10 ** 5
n = int(input())
s = list(input())

# a,t,c,o,d,e,rについてdp
dp = {'a': 0,'t':0,'c':0,'o':0,'d':0,'e':0,'r':0}
lst = list(dp)
for i in range(n):
    el = s[i]
    if el == 'a':
        dp[el] += 1
    elif el in lst:
        idx = lst.index(el)
        dp[el] += dp[lst[idx-1]]

print(dp['r']% (10**9+7))