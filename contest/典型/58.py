# max(n) = 10^5-1
# max(k) = 10^18
mod = 10 ** 5
x,k = input().split()
memo = {}

for i in range(int(k)):
    y = sum(map(int,list(x)))
    z = (int(x) + y) % mod
    if memo.get(z):
        # 何番めに出てきたか
        lst = list(memo.keys())
        # ループの最初のidx
        idx = lst.index(z)

        # ループの長さ
        loop = (i-1) - idx + 1

        # 今回を含めたボタンを押す残り
        remain = int(k)-(i+1)
        offset = remain % loop
        print(lst[idx+offset])
        break
    else:
        memo[z] = True
    x = str(z)
else:
    print(x)





