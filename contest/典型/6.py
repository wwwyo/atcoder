
# ! 辞書順で最小を求める=>greedy
n,k = map(int,input().split())
s = list(enumerate(input()))
# i番目以降の文字列の中で辞書最小が欲しい
# dpで後ろからとってくる
dp = [[None] * 26 for _ in range(n+1)]
for i,v in s[::-1]:
    j = ord(v) % 97
    dp[i] = dp[i+1][:]
    dp[i][j] = i
left = -1
cnt = 0
done = False
while not done:
    remain = k-cnt
    if remain == 0:
        done = True
        break

    lst = dp[left+1]
    for j in range(26):
        if lst[j] == None: continue
        if n-lst[j] >= remain:
            cnt +=1
            left = lst[j]
            print(chr(j + 97),end="")
            break

    # for i in range(n):
    #     # 選んだ数を含んで右にある配列の数が残りの文字列以上かつ
    #     # 以前選んだものより右にある必要がある
    #     right_len = n - s[i][0]
    #     if right_len >= remain and s[i][0] > left:
    #         left = s[i][0]
    #         cnt += 1
    #         print(s[i][1],end="")
    #         break



