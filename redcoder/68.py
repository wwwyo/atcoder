

n = int(input())
n_origin = n
is_prime = [0] * (n+1)
is_prime[0] = -1
is_prime[1]= -1
for i in range(2,n+1):
    if is_prime[i] == -1:
        continue
    for j in range(i*2,n+1,i):
        is_prime[j] = -1
    while n % i == 0:
        is_prime[i]+=1
        n//=i

ans = []
for i in range(n_origin+1):
    if is_prime[i] == -1:
        continue
    for _ in range(is_prime[i]):
        ans.append(i)
print(f"{str(n_origin)}:",*ans)








