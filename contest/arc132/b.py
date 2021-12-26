
# 10^5
n = int(input())
p = list(map(int,input().split()))

# 昇順に並べ替える
memo = {'>':-1,'<':-1}
token = ''
for i in range(n-1):
    if p[i] < p[i+1] :
        token = '<'
        # if memo['<'] != -1:
        #     continue
        # memo['<'] = i+1
    else:
        token = '>'
    if memo[token] != -1:
        continue
    memo[token] = i+1
    if memo['>'] != -1 and memo['<'] != -1:
        break
        # if memo['>'] != -1:
        #     continue
        # memo['>'] = i+1
if token == '>':
    if memo['<'] == -1:
        print(1)
        exit()
    ans = min(memo[token],2+n-memo[token])
else:
    if memo['>'] == -1:
        print(0)
        exit()
    ans = min(memo[token]+1, 1+n-memo[token])
print(ans)



