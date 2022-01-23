
# 10**5
n,m = map(int,input().split())
# n番目の駅
s = input().split()
s_dict = {i:0 for i in s}
#行列車 急
t = input().split()
for station in t:
    s_dict[station] = 1
for i in range(n):
    if s_dict[s[i]]:
        print('Yes')
    else:
        print('No')