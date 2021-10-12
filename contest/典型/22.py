import math
a,b,c = map(int,input().split())
# 最大公約数で割った時の商-1
gcd = math.gcd(math.gcd(a,b),c)
print((a // gcd -1)+(b // gcd -1)+(c // gcd -1))
