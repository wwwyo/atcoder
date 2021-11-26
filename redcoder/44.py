
# ! TLE
# def main():
#     ans = []
#     N = 10**6
#     dp = [10**10]*(N+1)
#     dp_odd = [10**10]*(N+1)
#     dp[0] = 0
#     dp_odd[0] = 0

#     for i in range(1,10**3):
#         w = i*(i+1)*(i+2)//6
#         if N<=w:
#             break
#         for n in range(N-w):
#             # dp[n+w] = min(dp[n]+1,dp[n+w]) # TLE
#             new = dp[n] + 1
#             if new < dp[n+w]:
#                 dp[n+w] = new
#         if w&1==1:
#             for n in range(N-w):
#                 #dp_odd[n+w] = min(dp_odd[n]+1,dp_odd[n+w]) # TLE
#                 new = dp_odd[n] + 1
#                 if new < dp_odd[n+w]:
#                     dp_odd[n+w] = new
                    
#     while(1):
#         S = int(input())
#         if S==0:break
#         ans.append([dp[S],dp_odd[S]])
#     for a,b in ans:
#         print(a,b)
# if __name__ == '__main__':
#     main()

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
