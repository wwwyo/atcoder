
# 10^5まで奇数列挙
q = int(input())
is_prime = [1] * (10**5+1)
is_prime[0] = is_prime[1] = 0
prime_dp = [0] * (10**5+1)
for i in range(2,10**5+1):
    if is_prime[i] == 0:
        prime_dp[i] = prime_dp[i-1]
        continue

    if is_prime[(i+1)//2]:
        prime_dp[i] = prime_dp[i-1] + 1
    else:
        prime_dp[i] = prime_dp[i-1]
    for j in range(i*2,10**5+1,i):
        is_prime[j] = 0

for _ in range(q):
    l,r = map(int,input().split())
    print(prime_dp[r]-prime_dp[l-1])

