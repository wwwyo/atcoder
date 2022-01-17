
# 1000
m,n = map(int,input().split())
# 10**5
k = int(input())

# dist = []
dp = [[[0,0,0] for _ in range(n+1)] for _ in range(m+1) ]
idx_dic = {'J':0,'O':1,'I':2}
# 1index
for i in range(1,m+1):
    dist = list(input())
    for j in range(1,n+1):
        idx = idx_dic[dist[j-1]]
        # dist[j] += [idx]
        for l in range(3):
            dp[i][j][l] = dp[i-1][j][l] + dp[i][j-1][l] - dp[i-1][j-1][l]
        dp[i][j][idx] += 1


for j in range(k):
    a,b,c,d = map(lambda x:int(x),input().split())
    ans = []
    for i in range(3):
        ans.append(dp[c][d][i]-dp[a-1][d][i]-dp[c][b-1][i]+dp[a-1][b-1][i])
    print(*ans)
    

# H, W = map(int, input().split())
# K = int(input())
# board = [input() for _ in range(H)]

# J = [[0]*(W + 1) for _ in range(H + 1)]
# O = [[0]*(W + 1) for _ in range(H + 1)]
# I = [[0]*(W + 1) for _ in range(H + 1)]
# for h in range(1, H + 1):
#    for w in range(1, W + 1):
#        J[h][w] = J[h - 1][w] + J[h][w - 1] - J[h - 1][w - 1]
#        O[h][w] = O[h - 1][w] + O[h][w - 1] - O[h - 1][w - 1]
#        I[h][w] = I[h - 1][w] + I[h][w - 1] - I[h - 1][w - 1]
#        if board[h - 1][w - 1] == "J":
#            J[h][w] += 1
#        if board[h - 1][w - 1] == "O":
#            O[h][w] += 1
#        if board[h - 1][w - 1] == "I":
#            I[h][w] += 1
           
# for _ in range(K):
#    a, b, c, d = map(int, input().split())
#    j = J[c][d] - J[a - 1][d] - J[c][b - 1] + J[a - 1][b - 1]
#    o = O[c][d] - O[a - 1][d] - O[c][b - 1] + O[a - 1][b - 1]
#    i = I[c][d] - I[a - 1][d] - I[c][b - 1] + I[a - 1][b - 1]
#    print(j, o, i)
