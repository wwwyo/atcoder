# やらかし
# ２桁目まで含まれるかチェックできてなかった
# memo= {0: 0, 1:1}

# def recursive(v):
#     if v-1 not in memo:
#         memo[v-1] = recursive(v-1)
#     memo[v] = 10 ** (v-1) + memo[v-1]
#     return memo[v]

# if __name__ == '__main__':
#     n = int(input())
#     ln = len(str(n))
#     if ln == 1:
#         print(1)
#         exit()

#     if int(str(n)[0]) > 1:
#         t = 10 **(ln-1)
#     else:
#         t = n - (10 ** (ln-1)) + 1
#     print(t + recursive(ln-1) +  sum(memo.values()))
    
# 方針
# 1
# 11
# 111で始まる数を調べる
# 1+1 - 1
# 11 + 1 - 11
# で調べることができる
n = int(input())
cnt = 0

for i in range(1,17):
    lead = int('1' * i)
    limit = lead + 1
    while lead <= n:
        cnt += min(n,limit-1) - lead + 1
        lead *= 10
        limit *= 10

print(cnt)




