import math
n = int(input())
primes = []
for i in range(2,int(n**0.5)+1):
    while n % i == 0:
        primes.append(i)
        n//=i
if n != 1:
    primes.append(n)
cnt = len(primes)
if cnt == 1:
    print(0)
else:
    print(math.ceil(math.log2(cnt)))