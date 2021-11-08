# n = 10^18
n,k = map(int,input().split())
mod = 10 ** 9 + 7

if n ==1:
    print(k %mod)
elif n == 2:
    print((k %mod) * ((k-1)%mod) %mod)
else:
    # 繰り返しに情報
    ans = (k %mod) * ((k-1)%mod) %mod
    n -=2
    k -=2
    # (k-2) **(n-2)
    while n:
        if n % 2:
            ans = ans * k %mod
        k =k * k %mod
        # 右シフト
        n >>= 1
    print(ans)

