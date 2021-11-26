
max_n = 10**6
# iを表現するのに必要な4面体の数
dp = [i for i in range(max_n+1)]
dp_odd = [i for i in range(max_n+1)]
tetra_lst = [i*(i+1)*(i+2)//6 for i in range(181)]


for i in range(2,max_n+1):
    for j in range(2,181):
        tetra = tetra_lst[j]
        if tetra > i:
            break
        if dp[i] > dp[i-tetra]+1:
            dp[i] = dp[i-tetra]+1
        if tetra % 2 == 1:
            if dp_odd[i] > dp_odd[i-tetra]+1:
                dp_odd[i] =dp_odd[i-tetra]+1




while True:
    n = int(input())
    if n == 0:
        break

    print(dp[n],dp_odd[n])
