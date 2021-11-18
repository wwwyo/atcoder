n = int(input())

memo = {0:1,1:1}
def fib(n):
    if memo.get(n):
        return memo[n]
    else:
        memo[n] = fib(n-1) + memo[n-2]
    return memo[n]
print(fib(n))